with start_station as (
    select
        start_station_id as station_id,
        start_station_name as station_name,
        start_lat as lat,
        start_lng as lng
    from {{ ref('stg_trips')}}
    where start_station_id is not null
),
end_station as (
    select
        end_station_id as station_id,
        end_station_name as station_name,
        end_lat as lat,
        end_lng as lng
    from {{ ref('stg_trips')}}
    where end_station_id is not null
),
base as (
    select * from start_station
    union all
    select * from end_station
),
stations as (
    select
        station_id,
        array_agg(
            station_name ignore nulls order by station_name limit 1
        )[safe_offset(0)] as station_name,
        avg(lat) as lat,
        avg(lng) as lng
    from base
    group by station_id
)
select
    row_number() over (order by station_id) as station_key,
    station_id,
    station_name,
    lat,
    lng
from stations

union all

select
    0 as station_key,
    'UNKNOWN' as station_id,
    'Unknown Station' as station_name,
    cast(null as float64) as lat,
    cast(null as float64) as lng