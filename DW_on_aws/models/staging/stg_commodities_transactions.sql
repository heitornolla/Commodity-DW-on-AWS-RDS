with source as (
    select
        date,
        symbol,
        action,
        quantity
    from 
        {{ source('awsdbt', 'commodities_transactions') }}
),

renamed as (
    select
        cast(date as date) as date,
        symbol as symbol,
        action as action,
        quantity as quantity
    from source
)

select
    date,
    symbol,
    action,
    quantity
from renamed