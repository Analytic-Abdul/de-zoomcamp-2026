-- =============================================
-- Module 3 Homework: Data Warehouse (BigQuery)
-- Yellow Taxi Trip Records: January - June 2024
-- =============================================

-- =============================================
-- SETUP: Create External Table from GCS
-- =============================================
-- NOTE: Replace 'your-project.your_dataset' with your actual project and dataset
-- NOTE: Replace 'your-bucket-name' with your actual GCS bucket name

CREATE OR REPLACE EXTERNAL TABLE `your-project.your_dataset.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://your-bucket-name/yellow_tripdata_2024-*.parquet']
);

-- SETUP: Create Materialized (regular) Table from External Table
CREATE OR REPLACE TABLE `your-project.your_dataset.yellow_tripdata_materialized` AS
SELECT * FROM `your-project.your_dataset.external_yellow_tripdata`;


-- =============================================
-- Question 1: Count of records for 2024 Yellow Taxi Data
-- Answer: 20,332,093
-- =============================================

SELECT COUNT(*) AS record_count
FROM `your-project.your_dataset.yellow_tripdata_materialized`;


-- =============================================
-- Question 2: Distinct PULocationIDs - External vs Materialized
-- Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table
-- =============================================

-- Query on External Table (check estimated bytes in the query validator)
SELECT COUNT(DISTINCT PULocationID)
FROM `your-project.your_dataset.external_yellow_tripdata`;

-- Query on Materialized Table (check estimated bytes in the query validator)
SELECT COUNT(DISTINCT PULocationID)
FROM `your-project.your_dataset.yellow_tripdata_materialized`;

-- External tables show 0 MB estimated because BigQuery cannot determine
-- the data size in advance for external data sources.
-- The materialized table shows ~155.12 MB because BigQuery knows the
-- exact column size stored internally.


-- =============================================
-- Question 3: Why are estimated bytes different for 1 vs 2 columns?
-- Answer: BigQuery is a columnar database, and it only scans the specific
-- columns requested in the query. Querying two columns (PULocationID,
-- DOLocationID) requires reading more data than querying one column
-- (PULocationID), leading to a higher estimated number of bytes processed.
-- =============================================

-- Query 1 column
SELECT PULocationID
FROM `your-project.your_dataset.yellow_tripdata_materialized`;

-- Query 2 columns
SELECT PULocationID, DOLocationID
FROM `your-project.your_dataset.yellow_tripdata_materialized`;


-- =============================================
-- Question 4: Records with fare_amount of 0
-- Answer: 8,333
-- =============================================

SELECT COUNT(*) AS zero_fare_count
FROM `your-project.your_dataset.yellow_tripdata_materialized`
WHERE fare_amount = 0;


-- =============================================
-- Question 5: Best strategy for optimized table
-- (filter on tpep_dropoff_datetime, order by VendorID)
-- Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID
-- =============================================

-- Partitioning by the datetime column used in WHERE filters reduces scan size.
-- Clustering by VendorID (used in ORDER BY) further optimizes within partitions.

CREATE OR REPLACE TABLE `your-project.your_dataset.yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `your-project.your_dataset.external_yellow_tripdata`;


-- =============================================
-- Question 6: Distinct VendorIDs between 2024-03-01 and 2024-03-15
-- Compare estimated bytes: materialized vs partitioned/clustered table
-- Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
-- =============================================

-- Query on Materialized (non-partitioned) table
-- Estimated: ~310.24 MB
SELECT DISTINCT VendorID
FROM `your-project.your_dataset.yellow_tripdata_materialized`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Query on Partitioned + Clustered table
-- Estimated: ~26.84 MB
SELECT DISTINCT VendorID
FROM `your-project.your_dataset.yellow_tripdata_partitioned_clustered`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';


-- =============================================
-- Question 7: Where is data stored in the External Table?
-- Answer: GCP Bucket
-- =============================================
-- External tables do not store data in BigQuery itself.
-- The data remains in the original GCS bucket and is read
-- at query time.


-- =============================================
-- Question 8: Is it best practice to always cluster data?
-- Answer: False
-- =============================================
-- Clustering is not always beneficial. For small tables,
-- the overhead of clustering may not provide performance gains.
-- Clustering is most effective on large tables (typically > 1 GB)
-- where queries frequently filter or aggregate on the clustered columns.


-- =============================================
-- Question 9 (Bonus): SELECT count(*) from materialized table
-- Answer: 0 Bytes
-- =============================================

SELECT COUNT(*)
FROM `your-project.your_dataset.yellow_tripdata_materialized`;

-- BigQuery stores metadata about the total number of rows in a table.
-- A COUNT(*) query does not need to scan any actual data because it can
-- be answered directly from the table metadata. Therefore, the estimated
-- bytes processed is 0 B.
