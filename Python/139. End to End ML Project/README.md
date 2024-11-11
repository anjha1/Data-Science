# FWI Prediction with Flask

This project provides a web interface for predicting the Fire Weather Index (FWI) using a Ridge regression model. The app accepts input parameters, scales them, and uses a pre-trained machine learning model to output a prediction of the FWI. This can help in assessing fire risk levels based on weather and environmental data.

## Project Structure

- **app.py**: The main Flask application, handling routing and predictions.
- **models/**: Directory containing the serialized Ridge regression model (`ridge.pkl`) and the StandardScaler (`scaler.pkl`) used to scale input data.
- **templates/**: Directory with HTML templates (`index.html` or `home.html`), which render the prediction interface.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- NumPy, Pandas, Scikit-learn
- Pickle

Install the dependencies with:

```bash
pip install flask numpy pandas scikit-learn
```

## Model Files

Ensure you have the following pre-trained model files in a `models/` directory:

- `ridge.pkl`: The Ridge regression model.
- `scaler.pkl`: The StandardScaler for scaling input features.

## Project Setup

1. **Clone or download the repository.**
2. **Navigate to the project directory**:
   ```bash
   cd fwi_prediction
   ```
3. **Run the Flask app**:
   ```bash
   python app.py
   ```
4. Open a browser and go to `http://0.0.0.0:5000` to access the application.

## Usage

1. Enter the required inputs:
   - Temperature
   - Relative Humidity (RH)
   - Wind Speed (Ws)
   - Rain
   - FFMC, DMC, ISI, Classes, Region

2. Click **Predict** to view the FWI prediction.

## File Overview

- **app.py**: Defines routes and prediction logic.
- **templates/home.html**: HTML file for the prediction form interface.
- **models/ridge.pkl** and **models/scaler.pkl**: The machine learning model and scaler files.

## Example Input

| Parameter   | Example Value |
|-------------|---------------|
| Temperature | 18.5          |
| RH          | 45            |
| Ws          | 10            |
| Rain        | 0.2           |
| FFMC        | 85            |
| DMC         | 200           |
| ISI         | 8             |
| Classes     | 2             |
| Region      | 3             |

## Troubleshooting

- **Model Not Found**: Ensure `ridge.pkl` and `scaler.pkl` are in the `models/` directory.
- **Module Not Found**: Ensure all dependencies are installed.

## Acknowledgments

Special thanks to Scikit-learn for machine learning support and Flask for the web framework.
