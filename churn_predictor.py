import pickle
import pandas as pd

with open("telecom_churn.pkl", "rb") as f:
    model = pickle.load(f)
new_customers = pd.DataFrame([
    {"tenure": 5, "monthly_charges": 70, "total_charges": 350, "num_calls": 120, "complaints": 2, "recharges": 3},
    {"tenure": 24, "monthly_charges": 40, "total_charges": 960, "num_calls": 200, "complaints": 0, "recharges": 12},
    {"tenure": 3, "monthly_charges": 90, "total_charges": 270, "num_calls": 80, "complaints": 5, "recharges": 1}
])

probs = model.predict_proba(new_customers)[:, 1]
segments = []
for p in probs:
    if p > 0.6:
        segments.append("At Risk")
    elif p < 0.3:
        segments.append("Loyal")
    else:
        segments.append("Dormant")

new_customers["churn_probability"] = probs.round(2)
new_customers["segment"] = segments

new_customers.to_csv("new_customer_predictions.csv", index=False)
print("✅ Predictions saved to new_customer_predictions.csv")
print(new_customers)
