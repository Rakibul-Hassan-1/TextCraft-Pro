import joblib
import pandas as pd

# Load model and vectorizer
model = joblib.load('models/model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Load test data
test_data = pd.read_csv('data/test_data.csv')

# Prepare test data
X_test = vectorizer.transform(test_data['text'])
predictions = model.predict(X_test)

# Display results
for text, pred, actual in zip(test_data['text'], predictions, test_data['sentiment']):
    print(f"Text: {text}")
    print(f"Predicted: {pred} | Actual: {actual}\n")

# Test custom input
custom_text = ["This was amazing!"]
custom_vector = vectorizer.transform(custom_text)
prediction = model.predict(custom_vector)[0]
print(f"\nCustom input prediction: '{custom_text[0]}' -> {prediction}")