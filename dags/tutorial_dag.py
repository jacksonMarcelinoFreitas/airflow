from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator #operador da task a ser utilizada - tipo python
from airflow.operators.bash import BashOperator
import pandas as pd 
import requests 
import json

def captura_conta_dados():
    url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json'
    response = request.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

def eh_valida(ti):
    qtd = ti.xcom_pull(task_id = 'captura_conta_dados')
    if(qtd > 1000):
        return 'valido'
    else:
        return 'nvalido'

# alocar recursos
with DAG('tutorial_dag', start_date = datetime(2023,8,17), schedule_interval = '30 * * * *', catchup=False) as dag:

    #task 1
    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = captura_conta_dados
    )

    eh_valida = BranchPythonOperator(
        task_id = "eh_valida",
        python_callable = eh_valida
    )

    #task 2
    valido = BashOperator(
        task_id = 'valido',
        bash_command = "echo 'Quantidade OK'"
    )

    #task 3
    nvalido = BashOperator(
        task_id = 'nvalido',
        bash_command = "echo 'Quantidade não OK'"
    )


captura_conta_dados >> eh_valida >> [valido, nvalido]

