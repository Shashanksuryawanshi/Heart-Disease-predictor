# Heart Disease Prediction Model

This repository contains a machine learning model that predicts whether an individual is at risk of heart disease. The model uses clinical and demographic data such as age, gender, blood pressure, cholesterol levels, and other health indicators. Additionally, the repository includes a Streamlit application for deploying the model in a user-friendly interface.

## Features
- **Data Preprocessing:** Handles missing values, normalization, and feature encoding.
- **Model Training:** Uses robust machine learning algorithms to ensure high accuracy.
- **Streamlit Deployment:** Interactive web application for real-time predictions.
- **Customizable:** Easily extendable with additional health indicators or datasets.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Libraries: 
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `streamlit`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ad1lhasan/heart-disease-predictor.git
   cd heart-disease-predictor
   ```
2. Install the required libraries as mentioned above.

### Files Included
- **HeartFailurePrediction.ipynb:** Jupyter notebook for exploratory data analysis and model training.
- **LICENSE:** License for the repository (MIT).
- **README.md:** Documentation for the repository.
- **features.csv:** File containing information about the features used in the model.
- **heart - heart.csv:** Dataset for training and testing the model.
- **heart.py:** Python script for deploying the Streamlit app.
- **random_forest_model.pkl:** Pre-trained Random Forest model.
- **scaler.pkl:** Scaler object for data normalization.

### Usage
1. Prepare your dataset in CSV format, similar to `heart - heart.csv`.
2. Run the preprocessing and training scripts using the notebook or provided files.
3. Launch the Streamlit app:
   ```bash
   app.py
   ```

### Example
```bash
app.py
```

### File Structure
```plaintext
.
.
your_project/
│
├── app.py                   # Main application file
├── heart.csv                # Data file
├── ML demo test.ppk         # PPK file for SSH
├── model.pkl                # Serialized machine learning model
├── requirements.txt         # Dependencies
├── static/                  # Static files (CSS, JavaScript, images)
│   └── ...
├── templates/               # HTML templates
│   └── ...
├── venv/                    # Virtual environment
│   └── ...
└── .gitignore               # Git ignore file

