# ml_model

import joblib
import numpy as np
import os

class Ml_Model:
    def __init__(self, model_path="utils/energy_model.joblib"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found {model_path}")
        self.model = joblib.load(model_path)

    def estimate(self, drone_pos, delivery_pos, current_energy=100):
        dx = abs(drone_pos[0] - delivery_pos[0])
        dy = abs(drone_pos[1] - delivery_pos[1])
        manhattan_distance = dx + dy

        features = np.array([[dx, dy, manhattan_distance]])
        prediction = self.model.predict(features)[0]

        return round(prediction) 
