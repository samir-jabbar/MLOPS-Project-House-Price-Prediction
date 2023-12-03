from flask import Flask, jsonify, request, render_template
import requests
app = Flask(__name__)

# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    return render_template('index.html')  # Use the HTML file with the form

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the form submission
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    sqft_living = request.form.get('sqft_living')
    view = request.form.get('view')
    grade = request.form.get('grade')
    sqft_above = request.form.get('sqft_above')
    yr_built = request.form.get('yr_built')
    sqft_living15 = request.form.get('sqft_living15')

    # Create input data dictionary
    input_data = {
        "bedrooms": int(bedrooms),
        "bathrooms": int(bathrooms),
        "sqft_living": int(sqft_living),
        "view": int(view),
        "grade": int(grade),
        "sqft_above": int(sqft_above),
        "yr_built": int(yr_built),
        "sqft_living15": int(sqft_living15)
    }

    # Make a POST request to the FastAPI predict endpoint
    response = requests.post(f"{FASTAPI_URL}/predict", json=input_data)

    if response.status_code == 200:
        prediction_result = response.json()
        return jsonify({'prediction_result': prediction_result})
    else:
        return jsonify({'error': 'Failed to get prediction from FastAPI.'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
