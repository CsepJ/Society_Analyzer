from requester import API_Request
from pathlib import Path
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

data_dir = Path(f"./{API_Request.folderName}")

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation="tanh"),
    tf.keras.layers.Dense(128, activation="tanh"),
    tf.keras.layers.Dense()
])
