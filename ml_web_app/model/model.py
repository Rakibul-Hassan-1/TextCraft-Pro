# Project Structure:
# - ml_web_app/
#   - static/
#     - style.css  # Updated for modern UI
#     - script.js  # Updated to handle user input
#   - templates/
#     - index.html  # Improved frontend design
#   - model/
#     - model.py
#     - __init__.py  # Ensures 'model' is recognized as a package
#   - app.py
#   - README.md
#   - model.pkl  # Trained model file

# Step 1: Train an Improved Disease Prediction Model

import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_diabetes

# Load dataset (use only glucose and BMI for this model)
data = load_diabetes()
X = data.data[:, [2, 3]]  # Using only glucose and BMI features
y = (data.target > 140).astype(int)  # Adjusted threshold for classification

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'model/model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')

# Prediction function
def predict(features):
    loaded_model = joblib.load('model/model.pkl')
    loaded_scaler = joblib.load('model/scaler.pkl')
    if features.shape[0] != 2:
        raise ValueError(f"Expected 2 features (Glucose & BMI), but got {features.shape[0]}")
    scaled_features = loaded_scaler.transform(features.reshape(1, -1))
    return int(loaded_model.predict(scaled_features)[0])

print("Improved model trained and saved!")