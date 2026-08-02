# Credit Card Fraud Detection

## Project Overview
A machine learning system to detect fraudulent credit card transactions using Random Forest classification. Built on a real-world dataset of 284,807 transactions with only 0.17% fraud rate.

## Problem Statement
Credit card fraud detection is a classic imbalanced classification problem. A naive model predicting all transactions as legitimate achieves 99.83% accuracy while catching zero fraud. This project addresses that challenge using proper techniques for imbalanced data.

## Dataset
- **Source:** Kaggle — Credit Card Fraud Detection
- **Size:** 284,807 transactions, 31 features
- **Fraud rate:** 0.17% (492 fraud cases)
- **Features:** V1-V28 (PCA transformed for privacy), Amount, Time

## Approach

### 1. Exploratory Data Analysis
- Identified severe class imbalance (0.17% fraud)
- Found Amount feature is heavily right-skewed
- Identified V14 and V17 as strongest predictors through correlation analysis
- Analyzed outliers using IQR method — retained them since fraudulent transactions often appear as outliers

### 2. Data Preprocessing
- Train/test split (80/20) with stratification to preserve fraud ratio
- Applied SMOTE to balance training data (492 → 227,451 fraud cases)
- StandardScaler for feature normalization (fit on train, transform on test to prevent data leakage)

### 3. Model
- **Algorithm:** Random Forest (100 trees)
- **Why Random Forest:** Handles non-linear patterns, provides feature importance, robust to imbalanced data

### 4. Results
| Metric | Score |
|--------|-------|
| Precision (Fraud) | 0.83 |
| Recall (Fraud) | 0.83 |
| F1-Score (Fraud) | 0.83 |
| ROC-AUC | 0.96 |

- Caught 81 out of 98 fraud cases in test set
- Only 17 false alarms on 56,864 legitimate transactions
- V14 identified as most important feature (confirmed by both EDA and model)

## Key Findings
- Transaction amount alone is not a strong fraud indicator
- V14 is the single most predictive feature (importance score: 0.22)
- SMOTE significantly improved fraud detection vs training on imbalanced data
- Retaining outliers was critical — 18.5% of fraud cases live in the outlier zone

## Tech Stack
- Python 3.9
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib

## How to Run
```bash
git clone https://github.com/LokeswarMaddika/detoml.git

## Dataset
Download creditcard.csv from https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
Place it in the fraud-detection/ folder before running the notebook.

cd detoml/week-03-classical-ml/fraud-detection
pip install -r requirements.txt
jupyter notebook fraud_detection.ipynb
```

## Author
Lokesh Maddika | Data Engineer → ML Engineer