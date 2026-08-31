from google.cloud import storage
from utils import get_logger

logger = get_logger(__name__)

def upload_gcs(bucket_name, year, csv_name, csv_content):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob_name = f"bronze/year={year}/{csv_name}"
    blob = bucket.blob(blob_name)
    blob.upload_from_string(csv_content, content_type="text/csv")
    logger.info(f"uploaded gs://{bucket_name}/{blob_name}")