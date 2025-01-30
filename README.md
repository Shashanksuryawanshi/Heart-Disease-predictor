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
   streamlit run heart.py
   ```

### Example
```bash
streamlit run heart.py
```

### File Structure
```plaintext
.
├── HeartFailurePrediction.ipynb
├── LICENSE
├── README.md
├── features.csv
├── heart - heart.csv
├── heart.py
├── random_forest_model.pkl
├── scaler.pkl
```

### Streamlit App
The Streamlit app provides an intuitive interface for users to input their health data and receive predictions. 

1. **Input Fields:** Enter details such as age, gender, cholesterol levels, blood pressure, etc.
2. **Predict Button:** Click the button to get the prediction result ("At Risk" or "Not At Risk").
3. **Visualization:** Displays visual summaries of the data and model insights.

## Acknowledgments
- Inspired by global efforts to improve early detection of heart disease.
- Thanks to the open-source community for providing excellent libraries and tools.
