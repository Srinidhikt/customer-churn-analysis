-- 1. Total call duration per customer
SELECT 
    customer_id,
    SUM(call_duration) AS total_call_duration
FROM 
    call_records
GROUP BY 
    customer_id;

-- 2. Average call duration per customer
SELECT 
    customer_id,
    AVG(call_duration) AS avg_call_duration
FROM 
    call_records
GROUP BY 
    customer_id;

-- 3. Count of complaints per customer
SELECT 
    customer_id,
    COUNT(complaint_id) AS num_complaints
FROM 
    complaints
GROUP BY 
    customer_id;

-- 4. Recharge frequency per customer
SELECT 
    customer_id,
    COUNT(recharge_id) AS recharge_frequency
FROM 
    recharges
GROUP BY 
    customer_id;

-- 5. Monthly charges, payment method and paperless billing
SELECT
    c.customer_id,
    b.monthly_charges,
    b.payment_method,
    b.paperless_billing
FROM
    customers c
JOIN
    billing b
ON
    c.customer_id = b.customer_id;
