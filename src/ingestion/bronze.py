from ingestion import upload_gcs, download_file, extract_csv
from utils import load_setting, get_logger
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import yaml

logger = get_logger(__name__)
setting = load_setting()

def process_month(year, month, base_url, bucket_name):
    zip_content = download_file(year, month, base_url)
    csv_name, csv_content = extract_csv(zip_content)
    upload_gcs(
        bucket_name=bucket_name,
        year=year,
        csv_name=csv_name,
        csv_content=csv_content,
    )
def main():
    bucket_name = setting.bucket_name
    with open(r"/opt/airflow/config/bronze.yml", "r") as f:
        config = yaml.safe_load(f)
    start_year = config["start_year"]
    start_month = config["start_month"]
    now = datetime.now()
    end_year = now.year
    end_month = now.month - 1
    jobs = []
    for year in range(start_year, end_year + 1):
        month_start = start_month if year == start_year else 1
        month_end = end_month if year == end_year else 12
        for month in range(month_start, month_end + 1):
            jobs.append((year, month))
    max_workers = 5
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(
                process_month,
                year,
                month,
                config['base_url'],
                bucket_name,
            )
            for year, month in jobs
        ]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f"Error: {e}")
                raise
if __name__ == "__main__":
    app = main()