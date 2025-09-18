import React, { useState, useEffect } from 'react';

interface TrafficData {
  vehicle_count: number;
  avg_speed: number;
  predicted_congestion_risk: number;
}

const riskLabels = ['Low', 'Medium', 'High'];

const UIFORSIH: React.FC = () => {
  const [traffic, setTraffic] = useState<TrafficData[]>([]);

  useEffect(() => {
    const fetchTraffic = async () => {
      const res = await fetch('/api/traffic');
      const data = await res.json();
      setTraffic(data);
    };
    fetchTraffic();
    const interval = setInterval(fetchTraffic, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Smart Traffic Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>Vehicle Count</th>
            <th>Avg Speed (km/h)</th>
            <th>Predicted Congestion Risk</th>
          </tr>
        </thead>
        <tbody>
          {traffic.map((row, idx) => (
            <tr key={idx}>
              <td>{row.vehicle_count}</td>
              <td>{row.avg_speed.toFixed(2)}</td>
              <td>{riskLabels[row.predicted_congestion_risk]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UIFORSIH;
