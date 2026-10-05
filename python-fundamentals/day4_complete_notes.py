# ============================================
# DAY 4 - COMPLETE NOTES
# Date: October 3-4, 2026
# ============================================

# ============================================
# SECTION 1: LAMBDA FUNCTIONS
# ============================================

# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# map - apply function to every element
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter - keep elements where condition is True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted with lambda - single criteria
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda x: x["grade"])

# sorted with lambda - multiple criteria
employees = [
    {"name": "Alice", "salary": 90000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 90000},
    {"name": "David", "salary": 60000}
]
# Sort by salary descending, then name ascending
sorted_employees = sorted(employees, key=lambda x: (-x["salary"], x["name"]))

# ============================================
# SECTION 2: PANDAS
# ============================================
import pandas as pd
import numpy as np

# Create DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 22],
    "salary": [70000, 85000, 90000, 75000, 65000],
    "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"]
}
df = pd.DataFrame(data)

# Basic exploration
df.head(3)          # first 3 rows
df.tail(2)          # last 2 rows
df.dtypes           # data types
df.describe()       # statistics summary
df.shape            # (rows, columns)
df.isnull().sum()   # missing values per column
df.isnull().sum().sum()  # total missing values

# Filtering
high_earners = df[df["salary"] > 75000]
engineers = df[df["department"] == "Engineering"]
# Multiple conditions - use & and ()
high_eng = df[(df["salary"] > 70000) & (df["department"] == "Engineering")]

# GroupBy
dept_avg = df.groupby("department")["salary"].mean()
dept_stats = df.groupby("department")["salary"].agg(["mean", "max", "min", "count"])

# Sorting
df_sorted = df.sort_values("salary", ascending=False)
df_sorted2 = df.sort_values(["department", "salary"], ascending=[True, False])

# Handling missing values
df.dropna()                           # drop rows with missing values
df.fillna(0)                          # fill with 0
df["age"].fillna(df["age"].mean())    # fill with mean

# Adding new columns
df["salary_monthly"] = df["salary"] / 12
df["senior"] = df["age"] > 30        # boolean column

# Method chaining
result = df.groupby("city")["score"].mean().sort_values(ascending=False).reset_index()

# reset_index() - converts grouped column back to regular column
# Without reset_index: grouped column becomes index
# With reset_index: grouped column becomes regular column

# ============================================
# SECTION 3: SQL
# ============================================

# INNER JOIN - only matching rows from both tables
"""
SELECT e.name, e.salary, d.name as department
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
"""

# LEFT JOIN - all rows from left table, NULL for non-matching right
"""
SELECT e.name, e.salary, d.name as department
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
"""

# GROUP BY + aggregations
"""
SELECT department_id, 
       COUNT(*) as employee_count,
       AVG(salary) as avg_salary,
       MAX(salary) as max_salary
FROM employees
GROUP BY department_id;
"""

# WHERE vs HAVING
# WHERE - filters rows BEFORE grouping
# HAVING - filters groups AFTER GROUP BY
"""
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 1;
"""

# Window Functions
"""
SELECT 
    name,
    salary,
    department_id,
    AVG(salary) OVER (PARTITION BY department_id) as dept_avg,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank_in_dept,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,
    LAG(num, 1) OVER (ORDER BY id) AS prev_value,
    LEAD(num, 1) OVER (ORDER BY id) AS next_value
FROM employees;
"""

# RANK vs DENSE_RANK vs ROW_NUMBER
# RANK()       - ties get same rank, next rank SKIPS    (1,2,2,4)
# DENSE_RANK() - ties get same rank, next rank NO SKIP  (1,2,2,3)
# ROW_NUMBER() - always unique, no ties                 (1,2,3,4)

# Top N per group pattern - MOST COMMON INTERVIEW QUESTION
"""
SELECT name, salary, department_id
FROM (
    SELECT name, salary, department_id,
        RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rnk
    FROM employees
) ranked
WHERE rnk = 1;
"""

# ============================================
# SECTION 4: LEETCODE SOLUTIONS
# ============================================

# Problem 49 - Group Anagrams
def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))  # sort letters = same key for anagrams
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

# Problem 347 - Top K Frequent Elements
def topKFrequent(nums, k):
    cnt = {}
    for num in nums:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
    sorted_cnt = sorted(cnt, key=lambda x: cnt[x], reverse=True)
    return sorted_cnt[:k]

# Problem 238 - Product of Array Except Self
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n  # initialize with 1s
    
    # Left pass - result[i] = product of everything to the LEFT
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right pass - multiply by product of everything to the RIGHT
    right_product = 1
    for i in range(n-1, -1, -1):  # iterate backwards
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# SQL LeetCode Solutions
"""
-- 175: Combine Two Tables (LEFT JOIN)
SELECT p.firstName, p.lastName, a.city, a.state 
FROM person p LEFT JOIN address a ON p.personId = a.personId;

-- 176: Second Highest Salary
SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary;

-- 177: Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N);
END

-- 178: Rank Scores
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores;

-- 180: Consecutive Numbers (LAG)
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1 AND num = prev2;

-- 181: Employees Earning More Than Managers (Self Join)
SELECT e2.name as Employee 
FROM employee e1 INNER JOIN employee e2 ON e1.id = e2.managerId 
WHERE e2.salary > e1.salary;

-- 184: Department Highest Salary (Correlated Subquery)
SELECT d.name as Department, e.name as Employee, e.salary as Salary 
FROM Employee e INNER JOIN Department d ON e.departmentId = d.id 
WHERE e.salary = (SELECT MAX(salary) FROM Employee WHERE departmentId = e.departmentId);
"""

# ============================================
# SECTION 5: DBT INTRO NOTES
# ============================================
"""
What is dbt?
- Data Build Tool - handles the T in ELT
- Write SQL SELECT statements, dbt handles CREATE TABLE/VIEW
- Version controlled in Git
- Built-in testing and documentation

Modern DE Stack:
Raw Data → S3 → Snowflake/BigQuery → dbt transforms → Analytics/ML

Key concepts:
- Models: SQL SELECT statements that become tables/views
- {{ ref('model_name') }}: how to reference other models
- Sources: declare raw data sources
- Tests: not null, unique, accepted values, relationships
- Incremental models: only process new/changed data
- Full refresh: reprocess everything

dbt vs Informatica (your experience):
- Same concept: transform raw data into clean tables
- dbt: SQL based, Git versioned, modern
- Informatica: GUI based, enterprise, legacy

Interview questions to prepare:
1. What is dbt and why use it over stored procedures?
2. What's the difference between a model and a source?
3. How does dbt handle dependencies between models?
4. What are dbt tests and why are they important?
5. What's the difference between incremental and full refresh?
"""

# ============================================
# SECTION 6: QUIZ WEAK AREAS TO REVIEW
# ============================================
"""
WEAK AREAS (scored low):
1. Fraud detection metrics - why not accuracy:
   - 99.83% transactions are legitimate
   - Model predicting all legitimate = 99.83% accuracy, catches ZERO fraud
   - Use: Precision, Recall, F1, ROC-AUC
   - Recall most important: missing real fraud costs bank money
   - Our model: Precision=0.83, Recall=0.83, ROC-AUC=0.96

2. Random Forest:
   - Builds 100 decision trees on random subsets of data and features
   - Majority vote for final prediction
   - Better than single tree: avoids overfitting
   - Why for fraud: handles non-linear patterns, gives feature importance
   - V14 was most important feature (importance score: 0.22)

3. Project walkthrough - practice this daily:
   "284,807 transactions, 0.17% fraud, 
   EDA found V14/V17 strongest predictors,
   kept outliers (18.5% fraud lives there),
   SMOTE balanced training data,
   fit_transform on train only (no leakage),
   Random Forest 100 trees,
   Results: Precision=0.83, Recall=0.83, ROC-AUC=0.96,
   Caught 81 of 98 fraud cases"
"""