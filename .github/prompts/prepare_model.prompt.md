---
description: "Generate a Python script to prepare a scikit-learn model for training on traffic data. The script should be functional with a mock dataset before the real data is available."
mode: "ask"
---
Your task is to act as a machine learning engineer and generate a Python script to prepare the AI predictive model for the Smart Traffic Management System.

The script must accomplish the following steps:

1.  **Set Up:** Include necessary library imports: `pandas`, `numpy`, and `sklearn.ensemble.RandomForestRegressor`. A RandomForestRegressor will be the basic model for this task.
2.  **Create Mock Data:** Since the real traffic data is not yet available, generate a small, synthetic dataset. This dataset must have two input features: `vehicle_count` and `avg_speed`. It should also have an output column named `congestion_risk` with discrete values (e.g., 0 for Low, 1 for Medium, 2 for High). The dataset should contain a few rows to represent different traffic scenarios.
3.  **Define the Model:** Instantiate the `RandomForestRegressor` model with a few basic hyperparameters.
4.  **Prepare a Training Function:** Write a function that takes the mock data as input, splits it into features and labels, and trains the regression model.
5.  **Test the Workflow:** Call the training function with the mock data to ensure that the entire process—from data loading to model training—works without errors.

The final output should be a single, well-commented Python file ready for execution.