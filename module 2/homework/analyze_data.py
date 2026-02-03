"""
Module 2 Homework - Data Analysis Script
This script downloads and analyzes NYC taxi data to answer the homework questions.
"""

import urllib.request
import gzip
import os

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download"

def download_file(url, local_path):
    """Download a file from URL to local path."""
    print(f"Downloading: {url}")
    urllib.request.urlretrieve(url, local_path)
    print(f"Downloaded to: {local_path}")

def get_uncompressed_size(gz_path):
    """Get the uncompressed size of a gzip file."""
    with gzip.open(gz_path, 'rb') as f:
        f.seek(0, 2)  # Seek to end
        size = f.tell()
    return size

def count_rows_in_gz_csv(gz_path):
    """Count rows in a gzipped CSV file (excluding header)."""
    count = 0
    with gzip.open(gz_path, 'rt', encoding='utf-8') as f:
        # Skip header
        next(f)
        for _ in f:
            count += 1
    return count

def format_size(size_bytes):
    """Format size in MiB."""
    return size_bytes / (1024 * 1024)

def main():
    print("=" * 60)
    print("Module 2 Homework - Data Analysis")
    print("=" * 60)

    # Question 1: Yellow Taxi 2020-12 uncompressed file size
    print("\n--- Question 1: Yellow Taxi 2020-12 uncompressed file size ---")
    yellow_2020_12_url = f"{BASE_URL}/yellow/yellow_tripdata_2020-12.csv.gz"
    yellow_2020_12_path = "yellow_tripdata_2020-12.csv.gz"

    if not os.path.exists(yellow_2020_12_path):
        download_file(yellow_2020_12_url, yellow_2020_12_path)

    # Get uncompressed size by reading the full file
    uncompressed_size = 0
    with gzip.open(yellow_2020_12_path, 'rb') as f:
        while True:
            chunk = f.read(1024 * 1024)  # Read 1MB at a time
            if not chunk:
                break
            uncompressed_size += len(chunk)

    print(f"Uncompressed file size: {format_size(uncompressed_size):.1f} MiB")

    # Question 2: Rendered value of variable (no download needed - it's a logic question)
    print("\n--- Question 2: Rendered variable value ---")
    print("When taxi=green, year=2020, month=04:")
    print("{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv")
    print("Renders to: green_tripdata_2020-04.csv")

    # Question 3: Yellow Taxi 2020 total rows
    print("\n--- Question 3: Yellow Taxi 2020 total rows ---")
    yellow_2020_total = 0
    for month in range(1, 13):
        month_str = f"{month:02d}"
        filename = f"yellow_tripdata_2020-{month_str}.csv.gz"
        url = f"{BASE_URL}/yellow/{filename}"

        if not os.path.exists(filename):
            download_file(url, filename)

        rows = count_rows_in_gz_csv(filename)
        print(f"  2020-{month_str}: {rows:,} rows")
        yellow_2020_total += rows

    print(f"Total Yellow Taxi 2020 rows: {yellow_2020_total:,}")

    # Question 4: Green Taxi 2020 total rows
    print("\n--- Question 4: Green Taxi 2020 total rows ---")
    green_2020_total = 0
    for month in range(1, 13):
        month_str = f"{month:02d}"
        filename = f"green_tripdata_2020-{month_str}.csv.gz"
        url = f"{BASE_URL}/green/{filename}"

        if not os.path.exists(filename):
            download_file(url, filename)

        rows = count_rows_in_gz_csv(filename)
        print(f"  2020-{month_str}: {rows:,} rows")
        green_2020_total += rows

    print(f"Total Green Taxi 2020 rows: {green_2020_total:,}")

    # Question 5: Yellow Taxi March 2021 rows
    print("\n--- Question 5: Yellow Taxi March 2021 rows ---")
    yellow_2021_03_url = f"{BASE_URL}/yellow/yellow_tripdata_2021-03.csv.gz"
    yellow_2021_03_path = "yellow_tripdata_2021-03.csv.gz"

    if not os.path.exists(yellow_2021_03_path):
        download_file(yellow_2021_03_url, yellow_2021_03_path)

    yellow_march_2021_rows = count_rows_in_gz_csv(yellow_2021_03_path)
    print(f"Yellow Taxi March 2021 rows: {yellow_march_2021_rows:,}")

    # Question 6: Timezone configuration (documentation question)
    print("\n--- Question 6: Timezone configuration ---")
    print("To configure timezone to New York in Kestra Schedule trigger:")
    print("Add a `timezone` property set to `America/New_York`")
    print("(Standard IANA timezone identifier)")

    # Summary
    print("\n" + "=" * 60)
    print("ANSWERS SUMMARY")
    print("=" * 60)
    print(f"Q1: Uncompressed file size = {format_size(uncompressed_size):.1f} MiB")
    print(f"Q2: Rendered value = green_tripdata_2020-04.csv")
    print(f"Q3: Yellow 2020 total rows = {yellow_2020_total:,}")
    print(f"Q4: Green 2020 total rows = {green_2020_total:,}")
    print(f"Q5: Yellow March 2021 rows = {yellow_march_2021_rows:,}")
    print(f"Q6: timezone property = America/New_York")

if __name__ == "__main__":
    main()
