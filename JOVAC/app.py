from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load the pre-trained model from the .pkl file
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define an endpoint to predict the score
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    
    if 'hours' not in data:
        return jsonify({'error': 'No input hours provided'}), 400
    
    try:
        hours = float(data['hours'])
    except ValueError:
        return jsonify({'error': 'Invalid input for hours. Must be a number.'}), 400
    
    # Predict the score using the loaded model
    predicted_score = model.predict(np.array([[hours]]))[0]
    
    # Return the predicted score as a JSON response
    return jsonify({'predicted_score': predicted_score})

if __name__ == '__main__':
    app.run(debug=True)