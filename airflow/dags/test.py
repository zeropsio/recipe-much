from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

my_dag = DAG(
    dag_id="my_dag_name",
    start_date=datetime(2024, 8, 2),
    schedule="* * * * *",
)

BashOperator(task_id="task", dag=my_dag, bash_command='echo "hello world"')