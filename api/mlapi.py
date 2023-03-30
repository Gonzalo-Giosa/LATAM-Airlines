import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import json

app = FastAPI()

class ScoringItem(BaseModel):
    dia:float
    mes:float
    km_ovsd:float
    t_media:float
    v_media_viento:float
    presion_media:float
    cantidad_de_lluvia_mm:float
    nubosidad_perc:float
    temporada_alta:float
    

with open('../dev/models/gbc_numpy_processing.pkl', 'rb') as f:
    model = pickle.load(f)
    
# levantar el json que tenga la info de train sobre la mediana, los minimos y los maximos
with open('stats_dict.json', "r") as json_file:
    # Load the JSON data into a dictionary
    stats_dict = json.load(json_file)
    
imputer = lambda x, median: np.where(np.isnan(x), median, x)
scaler = lambda x, f_min, f_max: (x - f_min) / (f_max - f_min)


def processing_payload(payload, lst_vars):
    
    payload_processed = payload.copy()

    medians = np.array([stats_dict[feature]["median"] for feature in lst_vars])
    f_mins = np.array([stats_dict[feature]["min"] for feature in lst_vars])
    f_maxs = np.array([stats_dict[feature]["max"] for feature in lst_vars])

    payload_processed = imputer(payload_processed, medians)
    payload_processed = scaler(payload_processed, f_mins, f_maxs)

    return payload_processed

lst_vars = ['dia',
 'mes',
 'km_ovsd',
 't_media',
 'v_media_viento',
 'presion_media',
 'cantidad_de_lluvia_mm',
 'nubosidad_perc',
 'temporada_alta'
 ]
    
    
@app.get('/')
async def health_check():
    return {"hello":"world"}


@app.post('/predict')
async def scoring_endpoint(item:ScoringItem):

    # 1: parsear el payload con numpy 
    data = np.array(list(item.dict().values())).reshape(1, -1)
    
    # 2: procesar la data usando custom functions basadas en numpy
    data_processed = processing_payload(payload=data, lst_vars=lst_vars)
    data_processed
    
    yhat = model.predict(data_processed)
    
    return {"prediction":int(yhat)}
