from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': "divvy",
    'retry_delay': timedelta(minutes=5),
    'retries': 5
}
with DAG (
    dag_id = "silver",
    schedule_interval = None,
    start_date = datetime(2025, 5, 5),
    catchup = False,
    max_active_runs = 1
) as dag:
    BashOperator(
        task_id = "divvy_transform",
        bash_command = f"docker exec spark-divvy spark-submit --master local[4] --driver-memory 6g --jars /opt/spark/extra_jars/gcs-connector-hadoop3-2.2.22-shaded.jar /opt/spark/src/transform/divvy.py"
    )