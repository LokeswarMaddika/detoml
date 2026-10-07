# ============================================
# DAY 5 - TUESDAY & WEDNESDAY NOTES
# Date: October 7-8, 2026
# ============================================

# ============================================
# SECTION 1: DBT COMPLETE PROJECT
# ============================================
"""
dbt Project Structure:
my_project/
├── dbt_project.yml      # project configuration
├── models/
│   ├── staging/         # raw data cleaning
│   └── marts/           # business logic
├── tests/               # data quality tests
├── macros/              # reusable SQL snippets
├── seeds/               # CSV files loaded as tables
└── snapshots/           # slowly changing dimensions

Three Layer Architecture:
Raw (sources) → Staging → Marts

Commands:
dbt init <project>     # create new project
dbt seed               # load CSV seed files
dbt run                # run all models
dbt test               # run all tests
dbt docs generate      # generate documentation
dbt docs serve         # open docs in browser

Models we built:
1. seeds/transactions.csv - raw data
2. models/staging/stg_transactions.sql - cleans data, adds amount_category
3. models/marts/mart_fraud_summary.sql - aggregates fraud by merchant

Materializations:
- view (default): query runs every time, no storage
- table: physical table stored, faster queries
- incremental: only processes new/changed data

Incremental model example:
{{ config(materialized='incremental') }}
SELECT * FROM {{ source('raw', 'transactions') }}
{% if is_incremental() %}
    WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
{% endif %}

Tests in schema.yml:
- unique
- not_null
- accepted_values
- relationships (foreign key check)

Macros - reusable SQL:
{% macro clean_amount(column_name) %}
    CASE WHEN {{ column_name }} < 0 THEN 0 ELSE {{ column_name }} END
{% endmacro %}

Key dbt interview questions:
Q1: What is dbt? → Transformation tool, handles T in ELT, SQL SELECT statements,
    adds version control/testing/docs to SQL
Q2: Incremental vs full refresh? → Incremental processes only new/changed data,
    full refresh reprocesses everything
Q3: What are dbt tests? → Generic (unique, not_null, accepted_values, relationships)
    and singular (custom SQL). Catch data quality issues before production.
Q4: Source vs model? → Source = raw table in warehouse dbt didn't create.
    Model = SQL SELECT that dbt transforms into table/view.
Q5: What are macros? → Reusable SQL snippets like Python functions.
    Used for standardization, null handling, env-specific logic.
"""

# ============================================
# SECTION 2: AIRFLOW CONCEPTS
# ============================================
"""
What is Airflow?
- Workflow orchestration tool
- Schedules, monitors, manages data pipelines
- The conductor that tells each part when to run and in what order

Problem it solves:
- Without Airflow: cron jobs with no dependency management, no retry, no monitoring
- With Airflow: dependency management, auto-retry, alerts, visual dashboard

Core Concepts:

DAG (Directed Acyclic Graph):
- Pipeline definition
- Directed: tasks flow one direction
- Acyclic: no circular dependencies
- Graph: tasks and their relationships

Operators (types of tasks):
- PythonOperator: runs Python function
- BashOperator: runs bash command
- SQLOperator: runs SQL
- S3ToRedshiftOperator: moves S3 data to Redshift

Task Dependencies:
extract >> transform >> load  # >> means "runs before"
task_a >> [task_b, task_c]   # parallel tasks
[task_a, task_b] >> task_c   # both must finish before c

Scheduling:
@daily          # every day at midnight
@hourly         # every hour
0 6 * * *      # every day at 6am
0 6 * * 1      # every Monday at 6am

Airflow vs dbt:
- dbt: transforms data INSIDE warehouse (T in ELT)
- Airflow: orchestrates ENTIRE pipeline including when dbt runs
- They work together: Airflow calls dbt

Example DAG:
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('fraud_pipeline', 
         start_date=datetime(2026,1,1), 
         schedule_interval='@daily') as dag:
    
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )
    
    transform = BashOperator(
        task_id='transform',
        bash_command='cd /dbt_project && dbt run'
    )
    
    load = PythonOperator(
        task_id='load',
        python_callable=load_data
    )
    
    extract >> transform >> load

Key features:
- Retries: automatically retry failed tasks
- Backfill: run pipeline for historical dates
- Web UI: visual dashboard
- XCom: pass data between tasks
- Connections: store credentials securely
"""

# ============================================
# SECTION 3: AWS S3 CONCEPTS
# ============================================
"""
What is S3?
- Simple Storage Service
- Object storage in the cloud
- Store any file type: CSV, JSON, Parquet, images, logs

Key Concepts:
- Buckets: container for files, globally unique name
- Objects: individual files with key (path) and value (content)

Three Data Lake Zones:
1. Raw zone: exact copy of source data, never modified
2. Processed zone: cleaned, transformed data
3. Curated zone: analytics-ready data

File Formats:
- CSV: simple, human readable, slow
- JSON: semi-structured, APIs
- Parquet: columnar, fast for analytics, MOST COMMON
- Avro: row-based, good for streaming

Why Parquet?
- Columnar: only reads columns you need
- Much faster and cheaper than CSV for large datasets

IAM (Identity and Access Management):
- Users: individual people
- Roles: permissions for services (Airflow needs role to read S3)
- Policies: rules defining allowed actions

S3 + Python (boto3):
import boto3
s3 = boto3.client('s3')

# Upload
s3.upload_file('local.csv', 'my-bucket', 'path/file.csv')

# Download
s3.download_file('my-bucket', 'path/file.csv', 'local.csv')

# Read directly into pandas
df = pd.read_csv('s3://my-bucket/transactions/file.csv')

Modern DE Stack:
Source → S3 (raw) → Snowflake/BigQuery → dbt → Analytics/ML
Airflow orchestrates the whole pipeline
"""

# ============================================
# SECTION 4: LEETCODE SOLUTIONS
# ============================================

# Problem 167 - Two Sum II (Two Pointer Pattern)
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1   # sum too small, move left right
        else:
            right -= 1  # sum too big, move right left

# Two Pointer Pattern:
# - Only works on SORTED arrays
# - Sum too small → move left pointer right (increases sum)
# - Sum too big → move right pointer left (decreases sum)
# - O(n) vs O(n²) brute force

# SQL Problem 185 - Department Top Three Salaries
"""
WITH high_sal AS (
    SELECT 
        d.name as Department, 
        e.name as Employee, 
        e.salary as Salary,
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) as rnk 
    FROM Employee e 
    JOIN Department d ON e.departmentId = d.id
)
SELECT Employee, Salary, Department 
FROM high_sal 
WHERE rnk < 4;

CTE vs Subquery:
- Both do the same thing
- CTE (WITH clause) is more readable
- Always use CTEs in interviews
"""

# ============================================
# SECTION 5: RESUME UPDATES MADE
# ============================================
"""
Changes made to resume:

1. Professional Summary updated:
"Data Engineer with 5+ years building production-scale data pipelines
for financial and regulatory reporting at Morgan Stanley and Amazon.
Proficient in Python, SQL, dbt, Spark, and AWS, with hands-on ML
engineering experience including fraud detection modeling using
Random Forest (ROC-AUC 0.96) on real financial data. Targeting
ML Engineer and senior Data Engineer roles at data-driven companies."

2. Projects section added:
- Credit Card Fraud Detection (Python, Scikit-learn, Random Forest)
  ROC-AUC 0.96, Recall 0.83, caught 81/98 fraud cases
- Fraud Data Pipeline (dbt, DuckDB, SQL)
  Staging + mart layers, tests, lineage graph

3. Skills updated:
- Added dbt, Airflow to ETL platforms
- Added Random Forest, SMOTE, Matplotlib to ML tools

4. Morgan Stanley new bullet:
"Designed input validation framework for regulatory pipelines,
reducing production incidents — applying statistical validation
concepts directly applicable to ML data preprocessing."

5. Years updated to 5+
"""

# ============================================
# SECTION 6: PLAN WHEN YOU RETURN OCT 13
# ============================================
"""
Monday Oct 13:
- LinkedIn optimization (headline, about, skills, projects)
- Start applying to jobs immediately
- Target companies: Stripe, Plaid, Databricks, Capital One, 
  Snowflake, fintech startups

Week of Oct 13:
- Apply to 5+ companies per day
- Airflow hands-on coding
- Continue LeetCode daily (1-2 problems)
- Mock interview prep

During travel (Oct 8-12):
- Practice fraud detection project walkthrough daily out loud
- 1 LeetCode problem per day on phone
- Read job descriptions at target companies
"""