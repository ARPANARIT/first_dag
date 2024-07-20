from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def print_test():
    print('This dag is to text git integration !')

dag = DAG(

    'test_dag',

    default_args={'start_date': days_ago(1)},

    schedule_interval='2 * * * *',

    catchup=False

)

only_task = PythonOperator(
    task_id ='print_test',
    python_callable = print_test,
    dag = dag
)

# dependency

only_task