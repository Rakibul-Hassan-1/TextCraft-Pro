import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# 1. Load data
train_data = pd.read_csv('data/training_data.csv')

# 2. Prepare features and labels
X = train_data['text']
y = train_data['sentiment']

# 3. Text vectorization (convert text to numbers)
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_vectors, y, test_size=0.2, random_state=42
)

# 5. Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Evaluate
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)
print(f"Training Accuracy: {accuracy_score(y_train, train_preds):.2f}")
print(f"Test Accuracy: {accuracy_score(y_test, test_preds):.2f}")

# 7. Save model and vectorizer
joblib.dump(model, 'models/model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Model training complete! Files saved in models/ directory")