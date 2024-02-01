from flask import Flask, request, jsonify
import pickle
#import pandas as pd
import numpy as np

import json

nisar = pickle.load(open('nisaran1.pkl', 'rb'))
flood = pickle.load(open('flood2.pkl', 'rb'))
earths = pickle.load(open('earth1.pkl', 'rb'))
stormm = pickle.load(open('strom.pkl', 'rb'))
tsunami = pickle.load(open('tsunami1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"



def earthss(Latitude, Longitude):
    input_querytyy1 = np.array([[Latitude, Longitude]])
    print(input_querytyy1)
    result2ea = earths.predict(input_querytyy1)[0]

    print(result2ea)
    return result2ea

def floods (ANNUAL_RAINFALL):
    input_q = np.array([[ANNUAL_RAINFALL]])
    result = flood.predict(input_q)[0]
    print(result)
    return result

def storm (Maximum_Wind):
    input_q = np.array([[Maximum_Wind]])
    result = stormm.predict(input_q)[0]
    print(result)
    return result


def tsunamis(latitude, longitude, Magnitude, Depth):
    input_q = np.array([[latitude,longitude,Magnitude,Depth]])
    result = tsunami.predict(input_q)[0]
    print(result)
    return result





@app.route('/dim', methods=['POST'])
def predict1():

    Latitude = request.form.get('Latitude')
    Longitude = request.form.get('Longitude')
    Soil_Type = request.form.get('Soil Type')
    Soil_weight = request.form.get('Soil weight')
    Region = request.form.get('Region')
    Capabilities = request.form.get('Capabilities')
    Rock_Type = request.form.get('Rock Type')
    Soil_Bearing_Capacity= request.form.get('Soil Bearing Capacity')
    Water_Depth = request.form.get('Water Depth')
    Structure_Type = request.form.get('Structure Type')
    Max_Water_Flow = request.form.get('Max Water Flow')
    Depth_Drill = request.form.get('Depth Drill')
    Maximum_Wind = request.form.get('Maximum Wind')

    ANNUAL_RAINFALL = request.form.get(' ANNUAL RAINFALL')

    #'Soil Type', 'Soil weight', 'Region', 'Capabilities','Rock Type', 'Soil Bearing Capacity', 'Water Depth', 'Structure Type','Max Water Flow','Depth Drill', 'Magnitude', 'Depth', 'Tsunami', 'Storm', 'Flood'

    Earthquake_Richter = earthss(Latitude,Longitude)
    print(Earthquake_Richter)
    Magnitude = Earthquake_Richter
    Depth = np.random.uniform(40, 100)
    storms  = storm(Maximum_Wind)
    print(storms)
    Floodpre = floods(ANNUAL_RAINFALL)
    print(Floodpre)
    tsunam = tsunamis(Latitude,Longitude,Magnitude,Depth)
    print(tsunam)

    input_query = np.array([[Soil_Type,Soil_weight,Region,Capabilities,Rock_Type,Soil_Bearing_Capacity,Water_Depth,Structure_Type,Max_Water_Flow,Depth_Drill,Magnitude,Depth,tsunam,storms,Floodpre]])
    print(input_query)
    result = nisar.predict(input_query)

    return jsonify({"Length": (result[0][0]), "Width":(result[0][1]),"Breadth":(result[0][2]), "Height":(result[0][3]), "Weight":(result[0][4]) })








if __name__ == '__main__':
    app.run(debug=True)





