from matplotlib import pyplot as plt
from pathlib import Path 
from requester import API_Request
import tensorflow as tf
import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import StandardScaler
model_path = "./model.h5"
scaler_path = "./scaler.pkl"
scaler = joblib.load(scaler_path)
model = tf.keras.models.load_model(model_path)
d = model.predict(np.array(scaler.transform(([[34020088, 4308, 97.16855413, 9.72047997, 76329.5822652029, 61.856]]))))
print(d)
d = model.predict(np.array(scaler.transform(([[36020088, 5008, 100, 39.72047997, 76329.5822652029, 61.856]]))))
print(d)