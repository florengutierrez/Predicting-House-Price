import pandas as pd
import numpy as np
from flask import Flask, request, Response, jsonify
from flask import render_template
from geopy.geocoders import Nominatim
import geocoder
import pickle

def function_address(address):
    
    try:
        response = geocoder.osm(address + ", Madrid").json
        
    except Exception as e: 
        response = None
        print(e)
    return response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.before_first_request
def startup():
    global model    

    filename = "./data/model_final.sav"
    model = pickle.load(open(filename, 'rb'))
    

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    if  request.method=="POST":
        array = make_array(**prepare_params(request.form))
        prediction = make_prediction(array)

        output = round(prediction[0])

        return render_template('index.html', prediction_text='El precio aproximado de tu vivienda es de {} €'.format(output))
    


def prepare_params(params):
    params = dict(params)
    for k,v in params.items():
        if k in ["sq_mt_built", "n_rooms", "n_bathrooms"]:
            params[k] = int(v)
        if k in ["is_new_development", "is_renewal_needed", "is_exterior", "has_garden", "has_pool", "has_terrace", "has_balcony", "has_parking"]:
            params[k] = 1 if v.lower() == "si" else 0
    coordinates = function_address(params["address"])
    params["lat"] = coordinates["lat"]
    params["lng"] = coordinates["lng"]
    return params

def make_array(sq_mt_built, n_rooms, n_bathrooms, is_renewal_needed, is_new_development,is_exterior, has_garden, has_pool, has_terrace, has_balcony,has_parking, lat, lng, **kwargs):
    return np.array([[sq_mt_built, n_rooms, n_bathrooms, 
       is_renewal_needed, is_new_development,
       is_exterior, has_garden, has_pool, has_terrace, has_balcony,
       has_parking, lat, lng]])

def make_prediction(arr):
    return model.predict(arr)


if __name__ == "__main__":
    
    app.run(debug=True)