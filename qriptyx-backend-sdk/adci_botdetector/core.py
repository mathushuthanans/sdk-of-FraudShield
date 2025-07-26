import pickle
import pandas as pd

class BotDetector:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        self.expected_features = list(self.model.feature_names_in_)

    def predict_from_dict(self, features: dict):
        data = pd.DataFrame([features], columns=self.expected_features)
        prediction = self.model.predict(data)[0]
        return int(prediction)
            

    def predict_from_list(self, feature_list: list):
        data = pd.DataFrame([feature_list], columns=self.expected_features)
        prediction = self.model.predict(data)[0]
        return int(prediction)
