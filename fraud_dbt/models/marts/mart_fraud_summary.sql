{{ config(materialized='table') }}

SELECT
    merchant,
    amount_category,
    COUNT(*) as total_transactions,
    SUM(is_fraud) as fraud_count,
    ROUND(SUM(is_fraud) * 100.0 / COUNT(*), 2) as fraud_rate_pct
FROM {{ ref('stg_transactions') }}
GROUP BY merchant, amount_category
ORDER BY fraud_rate_pct DESC