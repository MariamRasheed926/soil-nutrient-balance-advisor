# Soil Nutrient Balance Advisor

This project presents a machine learning system designed to analyze soil nutrient and moisture conditions and estimate their impact on crop productivity.

The system provides data-driven insights that can support better nutrient management and agricultural planning.

## Dataset

The project uses agricultural data containing:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Soil Moisture

The target variable represents estimated crop productivity.

## Model

A **Random Forest Regressor** is used to estimate crop productivity based on soil nutrient levels and moisture conditions.

The model identifies relationships between nutrient availability, soil moisture, and expected productivity.

## Performance

The reconstructed prototype achieved approximately:

* **R² Score:** 0.98
* **Mean Squared Error:** 31.92

These results were obtained using the reconstructed prototype dataset.

## Development Tools

Python
Pandas
NumPy
Scikit-learn
Random Forest Regressor
Machine Learning

## Future Development

Future improvements may include integrating additional soil properties, fertilizer information, irrigation data, and crop-specific nutrient requirements to provide more detailed nutrient management recommendations.
