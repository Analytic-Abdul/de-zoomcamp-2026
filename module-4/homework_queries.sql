-- =============================================
-- Module 4 Homework: Analytics Engineering with dbt
-- NYC Taxi Data (Green & Yellow, 2019-2020)
-- =============================================


-- =============================================
-- Question 3: Count of records in fct_monthly_zone_revenue
-- Answer: 12,998
-- =============================================

SELECT COUNT(*) AS record_count
FROM fct_monthly_zone_revenue;


-- =============================================
-- Question 4: Best performing zone for Green taxis (2020)
-- Answer: Morningside Heights
-- =============================================

SELECT
    pickup_zone,
    SUM(revenue_monthly_total_amount) AS total_revenue
FROM fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 5;


-- =============================================
-- Question 5: Green taxi trip counts (October 2019)
-- Answer: 384,624
-- =============================================

SELECT
    SUM(total_monthly_trips) AS total_trips
FROM fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND revenue_month = '2019-10-01';


-- =============================================
-- Question 6: Count of records in stg_fhv_tripdata
-- Answer: 42,084,899
-- =============================================

SELECT COUNT(*) AS record_count
FROM stg_fhv_tripdata;
