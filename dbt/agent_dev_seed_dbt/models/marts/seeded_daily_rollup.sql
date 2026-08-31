select
    current_date as metric_date,
    count(*) as customers,
    sum(revenue) as revenue
from {{ ref('seeded_customer_metrics') }}
