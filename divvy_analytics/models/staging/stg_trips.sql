select
    ride_id,
    rideable_type,
    started_at,
    ended_at,
    start_station_id,
    end_station_id,
    start_station_name,
    end_station_name,
    start_lat,
    end_lat,
    start_lng,
    end_lng,
    member_casual,
    timestamp_diff(ended_at, started_at, minute) as trip_duration_minutes
from {{ source('divvy_trip', 'trips')}}