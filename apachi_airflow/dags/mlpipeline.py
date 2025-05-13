import os 
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define Task 1: Preprocess Data
def preprocess_data():
    print("Preprocessing data...")
    # Your data preprocessing logic goes here


# Define Task 2: Train Model
def train_model():
    print("Training model...")
    # Your model training logic goes here


# Define Task 3: Evaluate Model
def evaluate_model():
    print("Evaluating model...")
    # Your model evaluation logic goes here


# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='ml_pipeline',
    default_args=default_args,
    description='A simple ML pipeline DAG',
    schedule_interval='@weekly',
    catchup=False,  # prevents backfilling when restarting Airflow
    tags=['machine_learning', 'example']
) as dag:

    preprocess = PythonOperator(
        task_id='preprocess_task',
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id='train_task',
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id='evaluate_task',
        python_callable=evaluate_model
    )

    # Set task dependencies
    preprocess >> train >> evaluate   
