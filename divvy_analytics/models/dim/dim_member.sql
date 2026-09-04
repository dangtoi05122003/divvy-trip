with base as (
    select distinct
        member_casual as member_type
    from {{ ref('stg_trips') }}
)
select
    row_number() over(order by member_type) as member_key,
    member_type
from base