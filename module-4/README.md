# Module 4 Homework: Analytics Engineering with dbt

## Setup

1. Set up the dbt project from `04-analytics-engineering/taxi_rides_ny/`
2. Load Green and Yellow taxi data (2019-2020) into your warehouse
3. Run `dbt build` to create all models and tests
4. For Question 6, also load FHV 2019 data

---

## Answers

### Question 1: dbt Lineage and Execution

> If you run `dbt run --select int_trips_unioned`, what models will be built?

**Answer: `int_trips_unioned` only**

`dbt run --select <model>` builds only the specified model. It does NOT automatically build upstream dependencies (you'd need `+int_trips_unioned` for that) and it does NOT build downstream models (you'd need `int_trips_unioned+` for that).

---

### Question 2: dbt Tests

> `accepted_values` test configured for payment_type with values [1,2,3,4,5]. A new value `6` appears. What happens when you run `dbt test --select fct_trips`?

**Answer: dbt will fail the test, returning a non-zero exit code**

The `accepted_values` test checks that all values in the column are within the configured list. Since `6` is not in `[1,2,3,4,5]`, the test finds rows that violate the constraint and fails. dbt does not skip tests, auto-update configs, or silently pass.

---

### Question 3: Count of records in `fct_monthly_zone_revenue`

```sql
SELECT COUNT(*) FROM fct_monthly_zone_revenue;
```

**Answer: 12,998**

---

### Question 4: Best performing zone for Green taxis (2020)

```sql
SELECT
    pickup_zone,
    SUM(revenue_monthly_total_amount) AS total_revenue
FROM fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 5;
```

**Answer: Morningside Heights**

---

### Question 5: Green taxi trip counts (October 2019)

```sql
SELECT
    SUM(total_monthly_trips) AS total_trips
FROM fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND revenue_month = '2019-10-01';
```

**Answer: 384,624**

---

### Question 6: Build staging model for FHV data

Created `stg_fhv_tripdata.sql` — a staging model that:
- Reads from the raw FHV 2019 trip data
- Renames `PUlocationID` / `DOlocationID` to `pickup_location_id` / `dropoff_location_id`
- Filters out records where `dispatching_base_num IS NULL`

```sql
SELECT COUNT(*) FROM stg_fhv_tripdata;
```

**Answer: 42,084,899**

---

## Files

| File | Description |
|------|-------------|
| `stg_fhv_tripdata.sql` | dbt staging model for FHV trip data (Question 6) |
| `homework_queries.sql` | SQL queries used for Questions 3-6 |
| `README.md` | This file — all answers and explanations |
