# Customer Churn Prediction

## Overview
This project predicts customer churn using a logistic regression model. The goal is to identify customers likely to leave and help businesses take preventive actions.

## Dataset
- \`customer_churn.xlsx\` — 999 records, 14 columns including tenure, charges, contract type, churn status, and customer demographics.

## Files
- \`churn_analysis.ipynb\` — Jupyter notebook with full workflow.
- \`churn_model.pkl\` — Saved trained model (optional).
- \`customer_churn.xlsx\` — Dataset (optional).

## Steps
1. Load and inspect data.
2. Preprocess: handle missing values, encode categorical variables.
3. Split into training and testing sets.
4. Train logistic regression model.
5. Evaluate using accuracy, confusion matrix, and classification report.

## Requirements
- Python
- pandas
- scikit-learn
- SHAP
- Jupyter Notebook

## How to Run
1. Place all files in the same folder.
2. Open \`churn_analysis.ipynb\` in Jupyter Notebook.
3. Run all cells sequentially to reproduce the results.
