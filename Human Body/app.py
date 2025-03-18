from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for model files

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_body_data', methods=['POST'])
def get_body_data():
    gender = request.json.get('gender', 'male')
    return jsonify({
        'male': {'head': [], 'chest': [], 'abdomen': []},
        'female': {'head': [], 'chest': [], 'abdomen': []}
    }[gender])

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)