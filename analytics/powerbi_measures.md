DAX Measures

Total Sales = SUM(sales_fact[amount])
Total Orders = COUNT(sales_fact[order_id])
Average Order Value = DIVIDE([Total Sales], [Total Orders])
