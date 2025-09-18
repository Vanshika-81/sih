import random
import pandas as pd

def fetch_time_distance(origin=None, destination=None, api_key=None):
    # Mock implementation: returns random time (min) and distance (km)
    return random.randint(5, 30), random.uniform(1, 10)

def compute_avg_speed_kmh(time_min, distance_km):
    if time_min == 0:
        return 0
    return (distance_km / (time_min / 60))

def simulate_vehicle_count():
    return random.randint(5, 120)

def generate_traffic_data(n=5):
    data = []
    for _ in range(n):
        time_min, distance_km = fetch_time_distance()
        avg_speed = compute_avg_speed_kmh(time_min, distance_km)
        vehicle_count = simulate_vehicle_count()
        data.append({
            'vehicle_count': vehicle_count,
            'avg_speed': avg_speed
        })
    return pd.DataFrame(data)

def simulate_signal_status():
    # Simulate status for 4 signals
    signals = ['A', 'B', 'C', 'D']
    status = {}
    for s in signals:
        status[s] = random.choice(['Green', 'Yellow', 'Red'])
    return status
