from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load model and scaler once to avoid redundancy
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

def predict(features):
    try:
        features = np.array(features, dtype=float).reshape(1, -1)  # Ensure correct shape
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        return int(prediction)  # Convert to integer for JSON compatibility
    except Exception as e:
        return str(e)  # Return error message for debugging

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        data = request.get_json()
        
        if 'features' not in data:
            return jsonify({'error': "Missing 'features' key in request data"}), 400
        
        features = np.array(data['features'], dtype=float)

        if features.shape != (2,):  # Ensure exactly 2 inputs (Glucose & BMI)
            return jsonify({'error': f'Expected 2 features (Glucose & BMI), but got {features.shape[0]}'}), 400

        prediction = predict(features)

        return jsonify({'prediction': prediction})  # 1 for High Risk, 0 for Low Risk
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
