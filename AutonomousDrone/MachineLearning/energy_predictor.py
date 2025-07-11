# energy_predictor

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("utils/energy_dataset.csv")

# Split features and label
X = df.drop("energy_consumed", axis=1)
y = df["energy_consumed"]

# Splits
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.125, random_state=42)  # 0.125 x 0.8 ≈ 0.1

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validation
val_preds = model.predict(X_val)
val_mae = mean_absolute_error(y_val, val_preds)
val_r2 = r2_score(y_val, val_preds)

print(f"--- VALIDATION ---")
print(f"MAE: {val_mae:.2f}")
print(f"R²: {val_r2:.2f}")

# Final evaluation
test_preds = model.predict(X_test)
test_mae = mean_absolute_error(y_test, test_preds)
test_r2 = r2_score(y_test, test_preds)

print(f"\n--- TEST ---")
print(f"MAE: {test_mae:.2f}")
print(f"R²: {test_r2:.2f}")

# Save model
joblib.dump(model, "utils/energy_model.joblib")
print("\nModelo guardado en utils/energy_model.joblib")
