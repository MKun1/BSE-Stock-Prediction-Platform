
import numpy
import sklearn
import tensorflow as tf
print("NumPy Version:", numpy.__version__)
print("scikit-learn Version:", sklearn.__version__)
print("TensorFlow Version:", tf.__version__)


import os
from tensorflow.keras.models import load_model

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "lstm_model.h5")
trained_model = load_model(model_path)


print("Model path:", model_path)
