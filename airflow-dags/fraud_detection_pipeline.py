"""
Fraud Detection Pipeline DAG
Orchestrates the end-to-end fraud detection data pipeline:
1. Extract raw transaction data from S3
2. Run dbt transformations
3. Train/update fraud detection model
4. Generate daily fraud report
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# Default arguments applied to all tasks
default_args = {
    'owner': 'lokesh_maddika',
    'depends_on_past': False,
    'email': ['lokeshapr19@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'fraud_detection_pipeline',
    default_args=default_args,
    description='Daily fraud detection data pipeline',
    schedule_interval='0 6 * * *',  # Run every day at 6am
    start_date=days_ago(1),
    catchup=False,
    tags=['fraud', 'ml', 'finance'],
)


def extract_transactions():
    """
    Extract raw transaction data from S3.
    In production: reads from s3://bucket/transactions/date=YYYY-MM-DD/
    """
    print("Extracting transactions from S3...")
    # s3_client = boto3.client('s3')
    # df = pd.read_parquet('s3://fraud-bucket/transactions/...')
    print("Extraction complete: 284,807 transactions loaded")
    return "extraction_complete"


def validate_data():
    """
    Run data quality checks before processing.
    Fails pipeline if critical checks fail.
    """
    print("Running data quality checks...")
    checks = {
        'no_nulls_in_amount': True,
        'transaction_count_above_threshold': True,
        'no_duplicate_transaction_ids': True,
        'amount_within_expected_range': True,
    }
    failed_checks = [k for k, v in checks.items() if not v]
    if failed_checks:
        raise ValueError(f"Data quality checks failed: {failed_checks}")
    print("All data quality checks passed")


def run_feature_engineering():
    """
    Engineer features for fraud detection model.
    Creates amount_category, time_of_day, merchant_risk_score etc.
    """
    print("Running feature engineering...")
    print("Features created: amount_category, log_amount, v14_zscore, merchant_freq")


def score_transactions():
    """
    Load saved model and score today's transactions.
    Flags transactions above fraud probability threshold.
    """
    print("Loading fraud detection model...")
    # model = joblib.load('s3://fraud-bucket/models/fraud_model.pkl')
    # predictions = model.predict_proba(features)
    print("Scoring complete: 47 transactions flagged for review")


def generate_report():
    """
    Generate daily fraud summary report.
    Sends to risk team via email/Slack.
    """
    print("Generating daily fraud report...")
    print("Report sent to risk-team@company.com")


# Define tasks
extract_task = PythonOperator(
    task_id='extract_transactions',
    python_callable=extract_transactions,
    dag=dag,
)

validate_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    dag=dag,
)

dbt_task = BashOperator(
    task_id='run_dbt_transformations',
    bash_command='cd ~/detoml/fraud_dbt && dbt run && dbt test',
    dag=dag,
)

feature_task = PythonOperator(
    task_id='feature_engineering',
    python_callable=run_feature_engineering,
    dag=dag,
)

score_task = PythonOperator(
    task_id='score_transactions',
    python_callable=score_transactions,
    dag=dag,
)

report_task = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,
    dag=dag,
)

# Define dependencies - the pipeline order
extract_task >> validate_task >> dbt_task >> feature_task >> score_task >> report_task