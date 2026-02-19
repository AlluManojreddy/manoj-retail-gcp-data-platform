from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="retail_data_platform_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    stream_task = BashOperator(
        task_id="run_dataflow_stream",
        bash_command="python dataflow/retail_stream_pipeline.py"
    )

    spark_task = BashOperator(
        task_id="run_spark_batch",
        bash_command="python dataproc/retail_batch_processing.py"
    )

    stream_task >> spark_task
