SELECT
    id,
    amount,
    UPPER(merchant) as merchant,
    is_fraud,
    CASE 
        WHEN amount > 1000 THEN 'high'
        WHEN amount > 100 THEN 'medium'
        ELSE 'low'
    END as amount_category
FROM {{ ref('transactions') }}