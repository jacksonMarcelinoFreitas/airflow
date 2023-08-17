## Arquivo para fins de estudos do Airflow

Neste arquivo estão algumas anotações sobre os recursos do airflow, aprendidos durante a fase de estudos da ferramenta. Tais como funções, dicas de uso, instalação e etc...

### Primeiro uso:

DAGs:
    São os arquivos python que compõem a estrutura visual do Airflow, nelas são definidos os fluxos de execuções, bem como funções para a execução de jobs. Suas tasks definidas por IDs, permitem a identificação inidividual destas no painel visual.
    # A DAG represents a workflow, a collection of tasks

- colocar imagem aqui

CRIAR DAG:

Imports utilizados:

    from airflow import DAG
    from datetime import datetime
    from airflow.operators.python import PythonOperator, BranchPythonOperator #operador da task a ser utilizada 
    from airflow.operators.bash import BashOperator


airflow.operators.python 


| Operador                   | Descrição                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------|
| PythonOperator             | Executa uma função Python.                                                                       |
| BranchPythonOperator       | Permite que um fluxo de trabalho siga um caminho após a execução dessa tarefa.                   |
| ShortCircuitOperator       | Permite que um pipeline continue com base no resultado de um python_callable.                    |
| PythonVirtualenvOperator   | Executa uma função em um ambiente virtual (virtualenv) que é criado e destruído automaticamente. |
| ExternalPythonOperator     | Executa uma função em um ambiente virtual (virtualenv) que não é recriado.                       |


Funções:

Parametros:

- python_callable ( Callable | None ) – Uma referência a um objeto que pode ser chamado
- op_kwargs – um dicionário de argumentos de palavras-chave que serão descompactados em sua função (modelo)
- op_args – uma lista de argumentos posicionais que serão descompactados ao chamar seu callable (modelado)
- multiple_outputs ( bool | None ) – se definido, o valor de retorno da função será desdobrado para vários valores XCom.

Parâmetros da DAG
- nome: 'tutorial_dag' 
- data de inicio: datetime(2023,8,17)
- intervalo de execução: '30 * * * *' - expressão [cron](https://en.wikipedia.org/wiki/Cron#CRON_expression)
- catchup=False - se sua DAG é limitada ao intervalo determinado ou não, criando uma execução somente para a DAG mais recente 

Ex:

    with DAG('tutorial_dag', start_date = datetime(2023,8,17), schedule_interval = '30 * * * *', catchup=False) as dag:

Definir sequência de execução:

Ao final do arquivo: 

Ex.:

    captura_conta_dados >> eh_valida >> [valido, nvalido]

