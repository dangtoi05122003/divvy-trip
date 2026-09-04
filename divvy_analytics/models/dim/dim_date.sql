with base as (
    select date(started_at) as date
    from {{ ref('stg_trips')}}
    union distinct
    select date(ended_at) as date
    from {{ ref('stg_trips')}}
)
select
    cast(format_date('%Y%m%d', date) as int64) as date_key,
    date,
    extract(year from date) as year,
    extract(quarter from date) as quarter,
    extract(month from date) as month,
    format_date('%Y-%m', date) as year_month,
    format_date('%A', date) as day_name
from base