import uvicorn
from fastapi import FastAPI
from variables import HouseVariables
import numpy
import pickle
import pandas as pd
import onnxruntime as rt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer

# Create app object 
app = FastAPI()

# Load model scalar
pickle_in = open("preprocessing.pkl", "rb")
scaler = pickle.load(pickle_in)

# Load the model
sess = rt.InferenceSession("model.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

# API Endpoints
@app.get('/')
def index():
    return {'Hello': 'Welcome to house price prediction service, access the api docs and test the API at http://0.0.0.0/docs.'}


@app.post('/predict')
def predict_house(data: HouseVariables):
    data = data.dict()

    # fetch input data using data varaibles
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    sqft_living = data['sqft_living']
    view = data['view']
    grade = data['grade']
    sqft_above = data['sqft_above']
    yr_built = data['yr_built']
    sqft_living15 = data['sqft_living15']

    data_to_pred = numpy.array([[bedrooms, bathrooms, sqft_living, view, grade, sqft_above, yr_built, sqft_living15]])

    # Scale input data
    #data_to_pred = scaler.fit_transform(data_to_pred.reshape(1, 8))
    
    # Model inference
    prediction = sess.run(
        [label_name], {input_name: data_to_pred.astype(numpy.float32)})[0]
    prediction = "House price is: " + str(prediction[0]) + " $" 
    return {
        'prediction': prediction
    }