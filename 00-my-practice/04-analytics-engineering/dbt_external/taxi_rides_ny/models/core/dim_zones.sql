{{
    config(
        materialized='table'
    )
}}

SELECT
    locationid,
    zone,
    replace(service_zone,'Boro','Green') as service_zone
FROM {{ ref('taxi_zone_lookup') }}