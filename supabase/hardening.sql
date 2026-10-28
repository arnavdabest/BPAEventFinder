-- Database-side limits. Run after schema.sql. Safe to re-run.
-- These hold even if someone skips the website and talks to the database directly.

-- Only known event types, small payloads, sane text lengths.
alter table events drop constraint if exists events_type_ok;
alter table events add constraint events_type_ok check (type in (
  'session_start','landing_view','quiz_start','question_view','option_toggle','answer','back',
  'quiz_complete','results_view','browse_all','detail_open','detail_close','link_click',
  'start_over','home_click','page_hidden'));
alter table events drop constraint if exists events_data_small;
alter table events add constraint events_data_small check (pg_column_size(data) <= 8192 and jsonb_typeof(data) = 'object');
alter table events drop constraint if exists events_qid_ok;
alter table events add constraint events_qid_ok check (question_id is null or question_id ~ '^[a-z]{1,20}$');

alter table sessions drop constraint if exists sessions_text_ok;
alter table sessions add constraint sessions_text_ok check (
  coalesce(char_length(referrer), 0) <= 500 and coalesce(char_length(landing_path), 0) <= 300
  and coalesce(char_length(utm_source), 0) <= 100 and coalesce(char_length(utm_medium), 0) <= 100
  and coalesce(char_length(utm_campaign), 0) <= 100 and coalesce(char_length(timezone), 0) <= 60
  and coalesce(char_length(language), 0) <= 20 and coalesce(char_length(country), 0) <= 5
  and coalesce(char_length(region), 0) <= 20 and (device is null or device in ('phone','tablet','desktop'))
  and coalesce(char_length(os), 0) <= 20 and coalesce(char_length(browser), 0) <= 20);

-- A real quiz run sends ~60 events. Cap each session at 400 so one bad actor can't fill the database.
create or replace function cap_session_events() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  if (select count(*) from public.events where session_id = new.session_id) >= 400 then
    raise exception 'event limit reached for this session' using errcode = 'P0001';
  end if;
  return new;
end $$;
drop trigger if exists cap_session_events on events;
create trigger cap_session_events before insert on events for each row execute function cap_session_events();

-- Daily job: keeps the free project awake and enforces the 2-year retention promised in the privacy policy.
create or replace function keepalive() returns int
language sql security definer set search_path = '' as $$
  delete from public.events   where created_at < now() - interval '2 years';
  delete from public.sessions where started_at < now() - interval '2 years';
  select 1;
$$;

-- "Delete my data": needs the browser's random anonymous ID, which can't be guessed.
create or replace function forget_visitor(p_vid uuid) returns void
language sql security definer set search_path = '' as $$
  delete from public.events   where visitor_id = p_vid;
  delete from public.sessions where visitor_id = p_vid;
$$;

-- Only these two functions are callable with the public key; trigger function is not.
revoke all on function cap_session_events() from public, anon, authenticated;
revoke all on function keepalive() from public, authenticated;
revoke all on function forget_visitor(uuid) from public, authenticated;
grant execute on function keepalive() to anon;
grant execute on function forget_visitor(uuid) to anon;

-- The public key can insert rows and nothing else.
revoke all on sessions, events from anon, authenticated;
grant insert on sessions, events to anon;
