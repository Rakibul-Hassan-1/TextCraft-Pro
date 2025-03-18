import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/test_reviews.csv")

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["review"])
y = df["sentiment"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model
with open("backend/model/sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("backend/model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved!")
