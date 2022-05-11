## Import packages
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import PythonOperator
from datetime import datetime
from datetime import date, timedelta


# Define default arguments
default_args = {
    'owner': 'Bykea',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(hours=1),
    'email': ['asra.khan@bykea.com'],
    'email_on_failure': False,
    'email_on_success': False,
    'email_on_retry': False,
    'max_active_runs':1,
    "catchup":False,
    'sla':timedelta(hours=1),
    'retries': 1,
    'retry_delay': timedelta(seconds=1),
}

DAG_NAME = 'dummy_dag'

dag = DAG(DAG_NAME,
 default_args=default_args, 
 concurrency=5,
 max_active_runs=1,
 schedule_interval=timedelta(minutes=30)
 )


dummy1 = DummyOperator(
    task_id="dummy1",
    dag = dag
)

dag >> dummy1

