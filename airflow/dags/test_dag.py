from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_test():
    print('This dag is to text git integration !')

dag = DAG(
    'test_dag',
    schedule_interval='0 12 * * *',
    catchup=False
)

only_task = PythonOperator(
    task_id='print_test',
    python_callable=print_test,
    dag = dag
)

# dependency

only_task