import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)

data = pd.DataFrame({
    "Nitrogen": np.random.uniform(20, 140, 1200),
    "Phosphorus": np.random.uniform(10, 100, 1200),
    "Potassium": np.random.uniform(10, 120, 1200),
    "Moisture": np.random.uniform(20, 80, 1200)
})

target = (
    30 +
    0.35 * data["Nitrogen"] +
    0.25 * data["Phosphorus"] +
    0.20 * data["Potassium"] +
    0.50 * data["Moisture"] -
    0.03 * (data["Nitrogen"] - 80) ** 2 -
    0.02 * (data["Moisture"] - 55) ** 2 +
    np.random.normal(0, 3, 1200)
)

X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"MSE: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")
