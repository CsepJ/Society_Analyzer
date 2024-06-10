from matplotlib import pyplot as plt
from pathlib import Path 
from requester import API_Request
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

infra_key = ["Airplane_Infra", "Train_Infra", "Internet_Infra", "Health_Infra", "Personal_GDP", "Labor_Participation"]
result = []
for c in API_Request.country_code:
    r = []
    t = []
    for i in infra_key:
        api_data = pd.json_normalize(API_Request().getData(c, i))
        api_data = api_data.fillna(round(sum(api_data.dropna().value)/len(api_data.dropna().date)))
        t.append(list(api_data.value))
    for a in range(len(t)):
        for b in range(len(t[a])):
            if len(r) <= b:
                r.append([t[a][b]])
            else:
                r[b].append(t[a][b])
    result.append(r)
x = result[0]
y = list(pd.read_csv("./data/Korea_Income.csv")["지니계수"])
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
epochs = 1000
model_path = "./model.h5"
scaler_path = "./scaler.pkl"
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, input_shape=(6,), activation="sigmoid"),
    tf.keras.layers.Dense(4, activation="sigmoid"),
    tf.keras.layers.Dense(1)
])

model.compile(loss="MeanSquaredError", optimizer="adam")
h = model.fit(np.array(x_scaled[16:43]),np.array(y), epochs=epochs)
loss = h.history["loss"]
epochs_range = range(epochs)
plt.figure()
plt.plot(epochs_range, loss)
plt.show()
pred = model.predict(np.array(scaler.transform([[726153000, 148553.0, 92.6, 16.57115173, 77000.0, 61.856]])))
model.save(model_path)
joblib.dump(scaler, scaler_path)
print(pred)
# model = tf.keras.models.load_model(model_path)
# d = model.predict(np.array([[726153000, 148553.0, 92.6, 77000.0, 61.856]]))
# print(d)
# x = np.array([[240,2], [350,-1], [800,4], [204,5], [10200,2], [3290,-1], [21,1], [40,0], [5300,0], [22, 30]])
# y = np.array([122, 179, 404, 107, 5102, 1644, 12, 20, 2650, 41])
# epochs = 50000
# model_path = "./model.h5"

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(128, input_shape=(2,), activation="relu"),
#     tf.keras.layers.Dense(64, activation="relu"),
#     tf.keras.layers.Dense(1)
# ])
# model.compile(loss="mse", optimizer="adam")
# h = model.fit(x,y, epochs=epochs)
# loss = h.history["loss"]
# epochs_range = range(epochs)
# plt.figure()
# plt.plot(epochs_range, loss)
# plt.show()
# pred = model.predict(np.array([[30000,1]]))
# model.save(model_path)
# print(pred)