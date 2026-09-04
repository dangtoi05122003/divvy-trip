with base as (
    select distinct
        rideable_type
    from {{ ref('stg_trips') }}
)
select
    row_number() over (order by rideable_type) as rideable_type_key,
    rideable_type
from base