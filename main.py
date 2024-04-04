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
     rock = {'Gneiss': 11, 'Schist': 12, 'Chalk': 13, 'Phonolite': 14, 'Syenite': 15, 'Limestone': 16,
           'Granite': 17, 'Basalt': 18, 'Sandstone': 19, 'Slit': 20, 'Volcanic Rocks': 21,
           'Flint': 22, 'Marl': 23, 'Shale': 24, 'Slate': 25, 'SlitStone': 26, 'Mudstone': 27,
           'SiltStone': 28, 'Steatite': 29, 'Ochre': 30, 'Calcite': 31, 'Kota Stone': 32,
           'Copper': 33, 'Marble': 34, 'Igneous': 35, 'Weathered': 36, 'Mineral Rock': 37,
           'Weathered Rocks': 38, 'Laterite ': 39, 'Clay': 40, 'Silt': 41, 'Glacier ': 42,
           'Metamorphoric': 43, 'Glacier Rock ': 44};
    capab = {'Good': 1, 'Better': 2, 'Very Hard': 3, 'Hard': 4, 'very Hard': 3, 'Easy': 0, 'Best': 5,
           'good': 1, 'Hard ': 4};
    strtype = {'Bridge': 1, 'Dam': 2, 'Building': 3};
    reg = {'Tropical ': 1, 'Semi-Arid': 2, 'Arid ': 3, 'River Valley': 4, 'Flood Plains': 5,
           'Indo Gangetic Plain': 6, 'Indo-Gangetic Plain': 7, 'Thar Desert': 8,
           'Northern Plain': 9, 'Deccan Plateau': 10, 'Malwa Plateau': 11,
           'Sahyadri Mountains': 12, 'Mediterranean': 13, 'Us Great Plains': 14,
           'Argentinian pampa': 15, 'Eastern Europe': 16, 'Midwest': 17, 'Deccan Trap': 18,
           'North Western': 19, 'Eastern Ghats': 20, 'Western Ghat': 21, 'Central India': 22,
           'Himalayas': 23, 'Northeastern': 24, 'North Eastern': 25, 'Peninsular ': 26,
           'western siberian Plain': 27, 'Russian Far East': 28,
           'Part of West Bengal': 29, 'Tamil Nadu Plateau': 30, 'Northern Plateau': 31,
           'Sundarbans': 32, 'Western Coasts': 33, 'Eastern Coast': 34, 'Eastern Plateau': 35,
           'Northwestern India': 36, 'Glaciated ': 37, 'Tropical': 38, 'River Deltas': 39,
           'Marshlands': 40, 'Taiga ': 41, 'Boreal': 42, 'Central Part of North America': 43,
           'Southern Gangetic Plain': 44, 'Chhattisgarh Plateau': 45, 'West Coast': 46,
           'Central Australia': 47, 'Southern Western US': 48, 'Nothern Africa': 49,
           'NorthEastern': 50, 'Northern Hemisphere': 51, 'Ganga Plain': 52,
           'Eastern Peninsular': 53};
    soil = {'Alfisols soil': 1, 'Alkaline Soil': 2, 'Alluvial Soil': 3, 'Arid Soil': 4,
           'Aridisol soil': 5, 'Azonal Soil': 6, 'Black Cotton Soil': 7, 'Brown Soil': 8,
           'Chalk Soil': 9, 'Chernozems Soil': 10, 'Chestnut Soil': 11, 'Clay Soil': 12,
           'Deltaic clay': 13, 'Desert Soil': 14, 'Entisols Soil': 15, 'Forest Soil': 16,
           'Gray Brown Soil': 17, 'Gray soil': 18, 'Histosols Soil': 19,
           'Inceptisols soil': 20, 'Laterite Soil': 21, 'Marshy Soil': 22,
           'Mollisols Soil': 23, 'Mountainous soil': 24, 'Oxisol soil': 25, 'Peat Soil': 26,
           'Podsols Soil': 27, 'Prairie Soil': 28, 'Red Soil': 29, 'Saline soil': 30,
           'Sandy loam': 31, 'Semi Arid soil': 32, 'Snowfields': 33, 'Spodosol Soil': 34,
           'Tundra soil': 35, 'Ultisol soil': 36, 'Yellow soil': 37, 'Zonal Soil': 38};
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

    input_query = np.array([[soil[Soil_Type] ,Soil_weight, reg[Region] ,  capab[Capabilities], rock[Rock_Type],Soil_Bearing_Capacity,Water_Depth, strtype[Structure_Type],Max_Water_Flow,Depth_Drill,Magnitude,Depth,tsunam,storms,Floodpre]])
    print(input_query)
    result = nisar.predict(input_query)

    return jsonify({"Length": (result[0][0]), "Width":(result[0][1]),"Breadth":(result[0][2]), "Height":(result[0][3]), "Weight":(result[0][4]) })








if __name__ == '__main__':
    app.run(debug=True)





