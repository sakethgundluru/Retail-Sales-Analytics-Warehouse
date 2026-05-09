SELECT SUM(sales) AS total_sales FROM sales;

SELECT COUNT(DISTINCT order_id) AS total_orders FROM sales;

SELECT COUNT(DISTINCT customer_id) AS total_customers FROM sales;

SELECT category, SUM(sales) AS category_sales
FROM sales
GROUP BY category
ORDER BY category_sales DESC;

SELECT region, SUM(sales) AS region_sales
FROM sales
GROUP BY region
ORDER BY region_sales DESC;

SELECT month, SUM(sales) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;

SELECT SUM(sales) / COUNT(DISTINCT order_id) AS avg_order_value
FROM sales;
