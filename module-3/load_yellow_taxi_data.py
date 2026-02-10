"""
Module 3 Homework - Data Loading Script
Downloads Yellow Taxi Trip Records (Jan-Jun 2024) and uploads to GCS.

Usage:
    1. Update BUCKET_NAME to your GCS bucket name
    2. Either set CREDENTIALS_FILE to your service account JSON path
       or authenticate via `gcloud auth application-default login`
    3. Run: python load_yellow_taxi_data.py
"""

import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from google.cloud import storage
from google.api_core.exceptions import NotFound, Forbidden
import time


# ============ CONFIGURATION ============
# Change this to your bucket name
BUCKET_NAME = "dezoomcamp_hw3_2026"

# Option 1: Service account credentials file
# CREDENTIALS_FILE = "gcs.json"
# client = storage.Client.from_service_account_json(CREDENTIALS_FILE)

# Option 2: Use default credentials (gcloud auth application-default login)
client = storage.Client()

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-"
MONTHS = [f"{i:02d}" for i in range(1, 7)]  # January to June
DOWNLOAD_DIR = "."
CHUNK_SIZE = 8 * 1024 * 1024  # 8 MB chunks for upload
# =======================================

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
bucket = client.bucket(BUCKET_NAME)


def download_file(month):
    """Download a single parquet file for the given month."""
    url = f"{BASE_URL}{month}.parquet"
    file_path = os.path.join(DOWNLOAD_DIR, f"yellow_tripdata_2024-{month}.parquet")

    try:
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded: {file_path}")
        return file_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None


def create_bucket(bucket_name):
    """Create the GCS bucket if it doesn't already exist."""
    try:
        bucket = client.get_bucket(bucket_name)
        project_bucket_ids = [b.id for b in client.list_buckets()]
        if bucket_name in project_bucket_ids:
            print(f"Bucket '{bucket_name}' exists and belongs to your project.")
        else:
            print(f"Bucket '{bucket_name}' exists but does not belong to your project.")
            sys.exit(1)
    except NotFound:
        bucket = client.create_bucket(bucket_name)
        print(f"Created bucket '{bucket_name}'")
    except Forbidden:
        print(f"Bucket '{bucket_name}' exists but is not accessible. Try a different name.")
        sys.exit(1)


def verify_gcs_upload(blob_name):
    """Verify that a blob exists in the bucket."""
    return storage.Blob(bucket=bucket, name=blob_name).exists(client)


def upload_to_gcs(file_path, max_retries=3):
    """Upload a file to GCS with retry logic."""
    blob_name = os.path.basename(file_path)
    blob = bucket.blob(blob_name)
    blob.chunk_size = CHUNK_SIZE

    for attempt in range(max_retries):
        try:
            print(f"Uploading {file_path} to {BUCKET_NAME} (Attempt {attempt + 1})...")
            blob.upload_from_filename(file_path)
            print(f"Uploaded: gs://{BUCKET_NAME}/{blob_name}")

            if verify_gcs_upload(blob_name):
                print(f"Verification successful for {blob_name}")
                return
            else:
                print(f"Verification failed for {blob_name}, retrying...")
        except Exception as e:
            print(f"Failed to upload {file_path} to GCS: {e}")

        time.sleep(5)

    print(f"Giving up on {file_path} after {max_retries} attempts.")


if __name__ == "__main__":
    create_bucket(BUCKET_NAME)

    # Download files concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:
        file_paths = list(executor.map(download_file, MONTHS))

    # Upload files concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(upload_to_gcs, filter(None, file_paths))

    print("All files processed and verified.")
