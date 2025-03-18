from flask import Flask, request, jsonify
import pickle

# Load trained model and vectorizer
with open("backend/model/sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("backend/model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review = data.get("review", "")
    transformed_review = vectorizer.transform([review])
    prediction = model.predict(transformed_review)[0]
    return jsonify({"sentiment": prediction})

if __name__ == "__main__":
    app.run(debug=True)
