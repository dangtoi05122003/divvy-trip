from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': "divvy",
    'retry_delay': timedelta(minutes=5),
    'retries': 5
}
with DAG (
    dag_id = "bronze",
    schedule_interval = None,
    start_date = datetime(2025, 5, 5),
    catchup = False,
    max_active_runs = 1
) as dag:
    BashOperator(
        task_id = "divvy_ingestion",
        bash_command = "cd /opt/airflow/src && python -m ingestion.bronze"
    )