import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

data = pd.DataFrame({
    'customer_id': range(1, 101),
    'call_duration': np.random.randint(50, 500, 100),
    'complaints': np.random.randint(0, 5, 100),
    'recharge_freq': np.random.randint(1, 10, 100),
    'monthly_charges': np.random.randint(100, 1000, 100),
    'paperless_billing': np.random.choice([0, 1], 100),
    'payment_method': np.random.choice([0, 1, 2], 100),
    'churn': np.random.choice([0, 1], 100, p=[0.7, 0.3])
})

X = data.drop(columns=['customer_id', 'churn'])
y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

y_pred_prob = model.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
auc = roc_auc_score(y_test, y_pred_prob)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.savefig("roc_curve.png")
plt.close()
print("✅ roc_curve.png saved")

coefficients = model.coef_[0]
features = X.columns

plt.figure(figsize=(8, 6))
plt.barh(features, coefficients)
plt.xlabel("Coefficient Value")
plt.title("Feature Importance (Logistic Regression)")
plt.tight_layout()
plt.savefig("feature_importance_coeff.png")
plt.close()
print("✅ feature_importance_coeff.png saved")
