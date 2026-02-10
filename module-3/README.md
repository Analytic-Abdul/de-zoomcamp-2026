# Module 3 Homework: Data Warehouse with BigQuery

## Dataset
Yellow Taxi Trip Records — **January 2024 to June 2024** (Parquet format)

Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Setup

### 1. Upload Data to GCS

Update the bucket name in `load_yellow_taxi_data.py`, then run:

```bash
pip install google-cloud-storage
python load_yellow_taxi_data.py
```

Verify that all 6 parquet files are in your GCS bucket before proceeding.

### 2. Create Tables in BigQuery

```sql
-- Create external table
CREATE OR REPLACE EXTERNAL TABLE `your-project.your_dataset.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://your-bucket-name/yellow_tripdata_2024-*.parquet']
);

-- Create materialized (non-partitioned, non-clustered) table
CREATE OR REPLACE TABLE `your-project.your_dataset.yellow_tripdata_materialized` AS
SELECT * FROM `your-project.your_dataset.external_yellow_tripdata`;
```

## Answers

### Question 1: Count of records for the 2024 Yellow Taxi Data

```sql
SELECT COUNT(*) FROM `your-project.your_dataset.yellow_tripdata_materialized`;
```

**Answer: 20,332,093**

---

### Question 2: Estimated data for distinct PULocationIDs (External vs Materialized)

```sql
-- External Table
SELECT COUNT(DISTINCT PULocationID)
FROM `your-project.your_dataset.external_yellow_tripdata`;

-- Materialized Table
SELECT COUNT(DISTINCT PULocationID)
FROM `your-project.your_dataset.yellow_tripdata_materialized`;
```

**Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table**

BigQuery cannot estimate scan size for external tables (shows 0 MB). For the materialized table, it knows the exact column size stored internally.

---

### Question 3: Why are estimated bytes different for 1 column vs 2 columns?

**Answer: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.**

---

### Question 4: Records with fare_amount of 0

```sql
SELECT COUNT(*)
FROM `your-project.your_dataset.yellow_tripdata_materialized`
WHERE fare_amount = 0;
```

**Answer: 8,333**

---

### Question 5: Best strategy for optimized table (filter by tpep_dropoff_datetime, order by VendorID)

```sql
CREATE OR REPLACE TABLE `your-project.your_dataset.yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `your-project.your_dataset.external_yellow_tripdata`;
```

**Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID**

Partitioning by the filter column reduces the amount of data scanned. Clustering by the ordering column optimizes data organization within each partition.

---

### Question 6: Estimated bytes — Materialized vs Partitioned table

```sql
-- Non-partitioned (materialized) table
SELECT DISTINCT VendorID
FROM `your-project.your_dataset.yellow_tripdata_materialized`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Partitioned + Clustered table
SELECT DISTINCT VendorID
FROM `your-project.your_dataset.yellow_tripdata_partitioned_clustered`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```

**Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table**

The partitioned table only scans the relevant date partitions (March 1-15), dramatically reducing the data processed.

---

### Question 7: Where is the data stored in the External Table?

**Answer: GCP Bucket**

External tables don't store data inside BigQuery. The data remains in the original GCS bucket and is read on-demand at query time.

---

### Question 8: Is it best practice to always cluster your data?

**Answer: False**

Clustering is not always beneficial. For small tables, the overhead may not provide performance gains. It's most effective on large tables (> 1 GB) with queries that frequently filter or aggregate on the clustered columns.

---

### Question 9 (Bonus): SELECT COUNT(*) estimated bytes

```sql
SELECT COUNT(*) FROM `your-project.your_dataset.yellow_tripdata_materialized`;
```

**Answer: 0 Bytes**

BigQuery stores table metadata including the total row count. A `COUNT(*)` query can be resolved from metadata alone without scanning any actual data, hence 0 bytes estimated.

## Files

| File | Description |
|------|-------------|
| `load_yellow_taxi_data.py` | Script to download parquet files and upload to GCS |
| `homework_queries.sql` | All SQL queries used to answer the homework questions |
| `README.md` | This file — solutions and explanations |
