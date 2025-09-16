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

if __name__ == "__main__":
    trained_model = train_model(df)
    print("Model training complete.")