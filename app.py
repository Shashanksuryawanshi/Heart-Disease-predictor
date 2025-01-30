from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sys

# Initialize Flask app
app = Flask(__name__)

# Load and prepare the dataset
try:
    df = pd.read_csv("heart.csv")  # Ensure correct filename
    X = df[['age', 'cp', 'thalach']]
    Y = df['target']
except FileNotFoundError:
    print("Error: Dataset not found. Please ensure 'heart_heart.csv' is in the project directory.")
    sys.exit()

# Train the logistic regression model
try:
    model = LogisticRegression(max_iter=1000)  # Ensure convergence
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    model.fit(X_train, Y_train)
    print("Model trained successfully.")
except Exception as e:
    print(f"Error during model training: {e}")
    sys.exit()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error_message = None

    if request.method == "POST":
        try:
            # Get input from the user
            age = request.form.get("age")
            cp = request.form.get("cp")
            thalach = request.form.get("thalach")

            # Validate user input
            if not age or not cp or not thalach:
                raise ValueError("All fields are required.")

            age, cp, thalach = int(age), int(cp), int(thalach)

            if age <= 0 or cp < 0 or thalach <= 0:
                raise ValueError("Inputs must be positive numbers.")

            # Ensure values are within reasonable ranges
            if age > 120:
                raise ValueError("Age must be between 1 and 120.")
            if cp not in [0, 1, 2, 3]:  # Based on standard heart dataset CP values
                raise ValueError("Chest pain type (cp) must be 0, 1, 2, or 3.")
            if thalach < 60 or thalach > 220:
                raise ValueError("Thalach (max heart rate) must be between 60 and 220.")

            # Make prediction
            user_data = np.array([[age, cp, thalach]])
            prediction = model.predict(user_data)[0]
            result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"

        except ValueError as ve:
            error_message = f"Input error: {ve}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"

    return render_template("index.html", result=result, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
