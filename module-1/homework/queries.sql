-- Homework Q3-Q6 SQL Queries
-- Run these in pgAdmin or psql after loading data

-- ============================================
-- Q3: Count trips with distance <= 1 mile
-- ============================================
-- Options: 7,853 | 8,007 | 8,254 | 8,421

SELECT COUNT(*) as short_trips
FROM green_taxi_data
WHERE trip_distance <= 1;

-- ============================================
-- Q4: Longest trip per day (exclude >= 100 miles)
-- ============================================
-- Options: 2025-11-14 | 2025-11-20 | 2025-11-23 | 2025-11-25
-- Find the pickup DATE with the longest single trip

SELECT
    DATE(lpep_pickup_datetime) as pickup_date,
    MAX(trip_distance) as max_distance
FROM green_taxi_data
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_distance DESC
LIMIT 1;

-- ============================================
-- Q5: Biggest pickup zone by total_amount on Nov 18
-- ============================================
-- Options: East Harlem North | East Harlem South | Morningside Heights | Forest Hills

SELECT
    z."Zone",
    SUM(g.total_amount) as total
FROM green_taxi_data g
JOIN taxi_zones z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total DESC
LIMIT 5;

-- ============================================
-- Q6: Largest tip for pickups from East Harlem North
-- ============================================
-- Options: JFK Airport | Yorkville West | East Harlem North | LaGuardia Airport

SELECT
    dz."Zone" as dropoff_zone,
    MAX(g.tip_amount) as max_tip
FROM green_taxi_data g
JOIN taxi_zones pz ON g."PULocationID" = pz."LocationID"
JOIN taxi_zones dz ON g."DOLocationID" = dz."LocationID"
WHERE pz."Zone" = 'East Harlem North'
GROUP BY dz."Zone"
ORDER BY max_tip DESC
LIMIT 5;
