from flask import Flask, jsonify
from flask_cors import CORS
from ml_model.model import train_model, df, predict_congestion_risk
from traffic_data_generator_googlemapsapi as well as mock data import generate_traffic_data, simulate_signal_status

app = Flask(__name__)
CORS(app)

# Train the model at startup
model = train_model(df)


@app.route('/api/traffic', methods=['GET'])
def get_traffic():
    # Generate new traffic data from the generator script
    traffic_data = generate_traffic_data()

    # Use your model to predict the congestion risk
    predictions = predict_congestion_risk(trained_model, traffic_data)

    # Add the prediction to each record in the traffic data
    for i, record in enumerate(traffic_data):
        record['congestion_risk'] = predictions[i]

    return jsonify(traffic_data)

@app.route('/api/signals', methods=['GET'])
def get_signals():
    status = simulate_signal_status()
    return jsonify(status)


