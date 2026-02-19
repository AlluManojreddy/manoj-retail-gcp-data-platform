CREATE TABLE retail_analytics_dw.sales_fact (
    order_id INT64,
    customer_id INT64,
    amount FLOAT64,
    owner STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(created_at)
CLUSTER BY customer_id;
