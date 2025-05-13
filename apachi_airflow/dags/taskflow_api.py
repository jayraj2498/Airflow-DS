from airflow import DAG 
from airflow.decorators import task 
from datetime import datetime, timedelta 

#define DAG 

with DAG(
    dag_id="math_sequence_dag_with_taskflow_api",
    start_date=datetime(2024, 1, 1),
    schedule_interval='@once',  # Correct argument name
    catchup=False,
) as dag :
    
        
    # task 1 : start with initial number 

    @task 
    def start_number() :
        initial_value = 10 
        print(f"starting number : {initial_value}") 
        return initial_value  
    
    # task 2 : add five to the number
    @task 
    def add_five(number) : 
        new_value = number + 5 
        print(f"add five :{number} + 5 = {new_value}")
        return new_value 
    
    
    # task 3 : multiply the number by two
    
    @task 
    def multiply_by_two(number):
        new_value = number* 2 
        print(f"multiply by two : {number} * 2 = {new_value}")
        return new_value 
    
    
    #task : sunstract 3 
    @task 
    def substract_by_three(number) :
        new_value = number - 3 
        print(f"subtract three : {number} - 3 = {new_value}")
        return new_value 
    
    
    @task 
    def square_number(number) :
        new_value = number ** 2 
        print(f"square number : {number} ** 2 = {new_value}")
        return new_value
    

    
    ## set task dependencies 
    
    start_val = start_number()
    added_values = add_five(start_val) 
    multiplied_values = multiply_by_two(added_values)
    substracted_values = substract_by_three(multiplied_values)
    squared_values = square_number(substracted_values)         
    
    
    