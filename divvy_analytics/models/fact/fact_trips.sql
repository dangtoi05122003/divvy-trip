select
    t.ride_id,
    d_start.date_key as start_date_key,
    d_end.date_key as end_date_key,
    m.member_key as member_key,
    r.rideable_type_key as rideable_type_key,
    coalesce(s_start.station_key, 0) as start_station_key,
    coalesce(s_end.station_key, 0) as end_station_key,
    t.trip_duration_minutes
from {{ref('stg_trips')}} t
left join {{ ref('dim_date')}} d_start on date(t.started_at) = d_start.date
left join {{ ref('dim_date')}} d_end on date(t.ended_at) = d_end.date
left join {{ref('dim_member')}} m on t.member_casual = m.member_type
left join {{ ref('dim_ride_type')}} r on r.rideable_type = t.rideable_type
left join {{ ref('dim_station')}} s_start on coalesce(t.start_station_id, 'UNKNOWN') = s_start.station_id
left join {{ ref('dim_station')}} s_end on coalesce(t.end_station_id, 'UNKNOWN') = s_end.station_id