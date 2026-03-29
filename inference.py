import joblib
import numpy as np
from sklearn.datasets import load_iris


def load_model():
    model = joblib.load("model.joblib")
    return model


def predict(model, data):
    features = np.array([[
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width']
    ]])
    prediction = model.predict(features)[0]

    iris = load_iris()
    target_names = iris.target_names[prediction]

    return str(target_names)