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

DAG_NAME = 'hello_world_dag'

dag = DAG(DAG_NAME,
 default_args=default_args, 
 concurrency=5,
 max_active_runs=1,
 schedule_interval=timedelta(minutes=30)
 )

def hello(context):
    print('HelloWorld')

hello = PythonOperator(
    task_id='hello_task',
    python_callable=hello,
    provide_context = True,
    xcom_push = True,
    xcom_all = True,
    dag=dag,
)

dag >> hello
