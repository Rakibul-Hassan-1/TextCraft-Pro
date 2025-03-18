from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('models/model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        text_vector = vectorizer.transform([text])
        prediction = model.predict(text_vector)[0]
        sentiment = prediction.capitalize()
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)