import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Create a mock dataset
data = {
    'vehicle_count': [10, 25, 40, 60, 80, 100],
    'avg_speed': [60, 45, 30, 25, 15, 10],
    'congestion_risk': [0, 0, 1, 1, 2, 2]  # 0: Low, 1: Medium, 2: High
}
df = pd.DataFrame(data)

# Define the model
model = RandomForestRegressor(random_state=42)

def train_model(df):
    features = df[['vehicle_count', 'avg_speed']]
    labels = df['congestion_risk']
    model.fit(features, labels)
    return model

def predict_congestion_risk(trained_model, traffic_data):
    """
    Predict congestion risk for each record in traffic_data using the trained model.

    Args:
        trained_model: Trained RandomForestRegressor model.
        traffic_data: List of dictionaries with 'vehicle_count' and 'avg_speed'.

    Returns:
        List of predicted congestion risk values (as integers).
    """
    df_input = pd.DataFrame(traffic_data)
    features = df_input[['vehicle_count', 'avg_speed']]
    predictions = trained_model.predict(features)
    return [int(round(pred)) for pred in predictions]

if __name__ == "__main__":
    trained_model = train_model(df)
    print("Model training complete.")