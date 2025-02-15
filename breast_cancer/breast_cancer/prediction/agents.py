# prediction/agent.py

import pickle
import numpy as np

# Load the trained model
def load_model():
    with open('prediction/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Function to make a prediction
def predict(features):
    model = load_model()
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]
