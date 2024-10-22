import joblib
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")
        self.scaler = joblib.load("artifacts/data_transformation/scaler.pkl")
        self.encoder = joblib.load("artifacts/data_transformation/encoder.pkl")

    def data_transform(self, data):
        # Separate numerical and categorical columns
        numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
        categorical_cols = ['cut', 'color', 'clarity']

        # Apply scaler to numerical columns
        num_data = data[numerical_cols]
        num_data_transformed = pd.DataFrame(self.scaler.transform(num_data),
                                    columns=numerical_cols)
        
        # Apply ordinal encoder to categorical columns
        cat_data = data[categorical_cols]
        cat_data_transformed = pd.DataFrame(self.encoder.transform(cat_data),
                                    columns=categorical_cols)
        
        # Combine the transformed numerical and categorical data
        data_transformed = pd.concat([num_data_transformed, cat_data_transformed], axis=1)

        return data_transformed
    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction