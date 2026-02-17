-- Staging model for For-Hire Vehicle (FHV) trip data (2019)
-- This model standardizes column names and filters out bad records
-- following the same patterns as stg_green_tripdata and stg_yellow_tripdata

with source as (
    select * from {{ source('raw', 'fhv_tripdata') }}
),

renamed as (
    select
        -- identifiers
        dispatching_base_num,
        cast(pulocationid as integer) as pickup_location_id,
        cast(dolocationid as integer) as dropoff_location_id,

        -- timestamps
        cast(pickup_datetime as timestamp) as pickup_datetime,
        cast(dropoff_datetime as timestamp) as dropoff_datetime,

        -- trip info
        sr_flag,
        affiliated_base_number

    from source
    -- Filter out records with null dispatching_base_num (data quality requirement)
    where dispatching_base_num is not null
)

select * from renamed
