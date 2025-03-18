sentiment-analysis-app/
│── backend/ # Backend (Flask)
│ ├── model/ # Model storage
│ │ ├── sentiment_model.pkl
│ │ ├── vectorizer.pkl
│ ├── app.py # Flask backend
│ ├── requirements.txt # Dependencies
│── frontend/ # Frontend (React)
│ ├── src/
│ │ ├── components/
│ │ │ ├── SentimentForm.js # Input form
│ │ │ ├── SentimentResult.js # Display result
│ │ ├── App.js # Main App
│ │ ├── index.js # Entry point
│ ├── package.json # Frontend dependencies
│── dataset/ # Data collection
│ ├── test_reviews.csv # Sample dataset
│ ├── preprocess.py # Data cleaning script
│── model_training/ # Model training
│ ├── train_model.py # Training script
│── README.md # Documentation
