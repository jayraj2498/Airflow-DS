from airflow import DAG 
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta 


# define function 

def start_number(**context): 
    context["ti"].xcom_push(key="current_value", value=10) 
    print("start_number 10") 


def add_five(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="start_task") 
    new_value = current_value + 5 
    context["ti"].xcom_push(key="current_value", value=new_value) 
    print(f"add 5 : {current_value} + 5 = {new_value}")


def multiply_by_two(**context): 
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="add_five_task") 
    new_value = current_value * 2 
    context["ti"].xcom_push(key="current_value", value=new_value) 
    print(f"multiply by 2 : {current_value} * 2 = {new_value}")


def subtract_three(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="mul_by_2_task")
    new_value = current_value - 3   
    context["ti"].xcom_push(key="current_value", value=new_value) 
    print(f"subtract 3 : {current_value} - 3 = {new_value}") 


def square_number(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="subtract_3_task") 
    new_value = current_value ** 2 
    context["ti"].xcom_push(key="current_value", value=new_value)
    print(f"square number : {current_value} ** 2 = {new_value}")
    


# define the DAG  

with DAG(
    'maths_sequence_operation',  
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Correct argument name
    catchup=False
) as dag:

    

    # define task 

    start_task = PythonOperator(
        task_id="start_task",
        python_callable=start_number,
        dag=dag
    ) 

    add_five_task = PythonOperator(
        task_id="add_five_task",
        python_callable=add_five,
        dag=dag
    ) 

    mul_by_2_task = PythonOperator(
        task_id="mul_by_2_task",
        python_callable=multiply_by_two,
        dag=dag
    )

    subtract_3_task = PythonOperator(
        task_id="subtract_3_task",  # Fixed typo in task_id
        python_callable=subtract_three,
        dag=dag
    )   

    square_number_task = PythonOperator(
        task_id="square_number_task",  # Fixed typo in task_id
        python_callable=square_number,
        dag=dag
    ) 


    # set the dependencies 

    start_task >> add_five_task >> mul_by_2_task >> subtract_3_task >> square_number_task








# from airflow import DAG 
# from airflow.operators.python import PythonOperator 
# from datetime import datetime, timedelta 


# # define function 

# def start_number(**context) : 
#     context["ti"].xcom_push(key="current_value", value=10) 
#     print("start_number 10") 
    
    
# def add_five(**context):
#     current_value = context["ti"].xcom_pull(key="current_value", task_ids="start_task") 
#     new_value = current_value + 5 
#     context["ti"].xcom_push(key="current_value", value=new_value) 
#     print(f"add 5 : {current_value} + 5 = {new_value}")



# def muliply_by_two(**context) : 
#     current_value = context["ti"].xcom_pull(key="current_value", task_ids="add_five_task") 
#     new_value = current_value * 2 
#     context["ti"].xcom_push(key="current_value", value=new_value) 
#     print(f"multiply by 2 : {current_value} * 2 = {new_value}")

    
# def subtract_three(**context) :
#     current_value = context["ti"].xcom_pull(key="current_value", task_ids="mul_by_2_task")
#     new_value = current_value - 3   
#     context["ti"].xcom_push(key="current_value", value=new_value) 
#     print(f"subtract 3 : {current_value} - 3 = {new_value}") 
    
    
# def square_number(**context):
#     current_value = context["ti"].xcom_pull(key="current_value", task_ids="subtract_3_task") 
#     new_value = current_value ** 2 
#     context["ti"].xcom_push(key="current_value", value=new_value)
#     print(f"square number : {current_value} ** 2 = {new_value}")
    
    
    
    
# # define the DAG  

# with DAG(
#     dag_id="maths_sequence_operation",
#     start_date=datetime(2024, 1, 1), 
#     schedule="@daily", 
#     catchup=False,
# ) as dag :
    
    

# # define task 

#     start_task = PythonOperator(
#         task_id = "start_task",
#         python_callable=start_number,
#         # provides_context=True,
#         dag=dag
#     ) 

#     add_five_task = PythonOperator(
#         task_id = "add_five_task",
#         python_callable=add_five,
#         # provides_context=True,
#         dag=dag
#     ) 

#     mul_by_2_task = PythonOperator(
#         task_id = "mul_by_2_task",
#         python_callable=muliply_by_two,
#         # provides_context=True,
#         dag=dag
#     )

#     subtract_3_task = PythonOperator(
#         task_id = "substract_3_task",
#         python_callable=subtract_three,
#         # provides_context=True,  
#         dag=dag
#     )   

#     square_number_task = PythonOperator(
#         task_id = "square_number_task",
#         python_callable=square_number,
#         # provides_context=True,
#         dag=dag
#     ) 



#     # set the dependencies 

#     start_task >> add_five_task >> mul_by_2_task >> subtract_3_task >> square_number_task