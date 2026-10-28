-- BPA Event Finder analytics schema. Paste into Supabase -> SQL Editor -> Run.
-- Anonymous only: no names, emails, or IP addresses are stored.
-- RLS: the public (publishable) key may only INSERT. Nobody can read rows except through the Supabase dashboard.

create table if not exists sessions (
  session_id   uuid primary key,
  visitor_id   uuid not null,          -- random id kept in the browser, so repeat visits link up
  started_at   timestamptz not null default now(),
  visit_number int,                    -- 1 = first time on the site
  referrer     text,
  utm_source   text, utm_medium text, utm_campaign text,
  landing_path text,
  country      text, region text,      -- from Vercel's edge (state/province level, no city, no IP)
  timezone     text,
  language     text,
  device       text,                   -- phone / tablet / desktop
  os           text, browser text,
  screen_w     int, screen_h int, viewport_w int, viewport_h int,
  dark_mode    boolean,
  touch        boolean
);

create table if not exists events (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  client_ts   timestamptz,
  session_id  uuid not null,
  visitor_id  uuid not null,
  type        text not null,           -- see README "What gets tracked"
  question_id text,
  data        jsonb not null default '{}'::jsonb
);
create index if not exists events_session_idx on events (session_id);
create index if not exists events_type_idx on events (type, created_at);

alter table sessions enable row level security;
alter table events   enable row level security;
drop policy if exists "anon insert sessions" on sessions;
drop policy if exists "anon insert events" on events;
create policy "anon insert sessions" on sessions for insert to anon with check (true);
create policy "anon insert events" on events for insert to anon with check (true);
revoke select, update, delete, truncate on sessions, events from anon, authenticated;

-- ---------- ready-made reports (Table Editor -> Views, or `select * from v_...`) ----------

-- One row per finished quiz with every answer as readable text and the picks it produced.
create or replace view v_completed_quizzes with (security_invoker = on) as
select e.created_at, e.session_id, e.visitor_id, s.country, s.region, s.device,
       e.data->'answers'     as answers,
       e.data->'interests'   as interests,
       e.data->'classes'     as classes,
       e.data->'mains'       as main_picks,
       e.data->'alternates'  as alternates,
       (e.data->>'total_ms')::int / 1000 as seconds_to_finish
from events e left join sessions s using (session_id)
where e.type = 'quiz_complete';

-- How popular each hobby / subject / class is.
create or replace view v_interest_popularity with (security_invoker = on) as
select 'interest' as kind, x as value, count(*) as picks
from events, jsonb_array_elements_text(data->'interests') x where type = 'quiz_complete' group by x
union all
select 'class', x, count(*)
from events, jsonb_array_elements_text(data->'classes') x where type = 'quiz_complete' group by x
order by kind, picks desc;

-- Every option of every question with how many people picked it (final answers only).
create or replace view v_answer_breakdown with (security_invoker = on) as
select question_id, data->>'question' as question, opt as answer, count(*) as picks,
       round(100.0 * count(*) / sum(count(*)) over (partition by question_id), 1) as pct
from events, jsonb_array_elements_text(data->'labels') opt
where type = 'answer'
  and not exists (select 1 from events later where later.session_id = events.session_id
                  and later.type = 'answer' and later.question_id = events.question_id and later.id > events.id)
group by question_id, data->>'question', opt
order by question_id, picks desc;

-- Funnel: how many sessions reached each question, and where people quit.
create or replace view v_funnel with (security_invoker = on) as
select step, question_id, count(distinct session_id) as sessions
from (select (data->>'step')::int as step, question_id, session_id from events where type = 'question_view') q
group by step, question_id order by step;

-- How long people spend on each question (seconds), and how often they change their answer.
create or replace view v_question_time with (security_invoker = on) as
select question_id, count(*) as answers,
       round((percentile_cont(0.5) within group (order by (data->>'ms')::numeric) / 1000)::numeric, 1) as median_seconds,
       round(avg((data->>'ms')::numeric) / 1000, 1) as avg_seconds,
       count(*) filter (where (data->>'changed')::boolean) as times_changed
from events where type = 'answer' group by question_id order by question_id;

-- Which events get recommended most, and as what.
create or replace view v_recommended_events with (security_invoker = on) as
select p->>'code' as code, p->>'name' as event, role, count(*) as times
from (
  select jsonb_array_elements(data->'mains') p, 'main' as role from events where type = 'quiz_complete'
  union all select jsonb_array_elements(data->'alternates'), 'alternate' from events where type = 'quiz_complete'
  union all select jsonb_array_elements(data->'addons'), 'add-on' from events where type = 'quiz_complete'
) t group by 1, 2, 3 order by times desc;

-- Which event cards people actually open to read more about (real interest signal).
create or replace view v_event_interest with (security_invoker = on) as
select data->>'code' as code, data->>'name' as event,
       count(*) filter (where type = 'detail_open') as detail_opens,
       count(distinct session_id) filter (where type = 'detail_open') as people,
       round(avg((data->>'ms')::numeric) filter (where type = 'detail_close') / 1000, 1) as avg_read_seconds,
       count(*) filter (where type = 'link_click') as link_clicks,
       count(*) filter (where type = 'detail_open' and data->>'from' = 'results') as opened_from_results,
       count(*) filter (where type = 'detail_open' and data->>'from' = 'all') as opened_from_browse_all
from events where type in ('detail_open', 'detail_close', 'link_click') and data ? 'code'
group by 1, 2 order by detail_opens desc;

-- Daily traffic.
create or replace view v_daily with (security_invoker = on) as
with s as (select started_at::date as day, count(*) as sessions, count(distinct visitor_id) as visitors,
                  count(*) filter (where visit_number = 1) as new_visitors from sessions group by 1),
     q as (select created_at::date as day, count(*) as quizzes_finished from events where type = 'quiz_complete' group by 1)
select s.*, coalesce(q.quizzes_finished, 0) as quizzes_finished
from s left join q using (day) order by day desc;

-- Where people come from.
create or replace view v_traffic_sources with (security_invoker = on) as
select coalesce(utm_source, nullif(split_part(split_part(referrer, '://', 2), '/', 1), ''), 'direct') as source,
       country, region, device, count(*) as sessions
from sessions group by 1, 2, 3, 4 order by sessions desc;

-- Used by the daily keep-alive ping so the free project never pauses.
create or replace function keepalive() returns int language sql security definer as $$ select 1 $$;

revoke all on v_completed_quizzes, v_interest_popularity, v_answer_breakdown, v_funnel, v_question_time,
  v_recommended_events, v_event_interest, v_daily, v_traffic_sources from anon, authenticated;
