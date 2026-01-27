#!/usr/bin/env python3
"""Load green taxi and zone data into PostgreSQL."""

import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

print("Loading green taxi data...")
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
print(f"  Loaded {len(df_green)} rows")
print(f"  Columns: {list(df_green.columns)}")

# Load to postgres
print("Writing green_taxi_data to PostgreSQL...")
df_green.to_sql('green_taxi_data', engine, if_exists='replace', index=False)
print("  Done!")

print("\nLoading taxi zone lookup...")
df_zones = pd.read_csv('taxi_zone_lookup.csv')
print(f"  Loaded {len(df_zones)} rows")

print("Writing taxi_zones to PostgreSQL...")
df_zones.to_sql('taxi_zones', engine, if_exists='replace', index=False)
print("  Done!")

print("\n=== Data loaded successfully! ===")
print(f"green_taxi_data: {len(df_green)} rows")
print(f"taxi_zones: {len(df_zones)} rows")
