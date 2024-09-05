from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('classifier.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('prdiction.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    age = int(request.form['age'])
    gender = request.form['gender']
    education_level = request.form['education_level']
    job_title = request.form['job_title']
    years_of_experience = int(request.form['years_of_experience'])

    # Encode categorical features
    gender = 1 if gender.lower() == 'male' else 0
    education_mapping = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
    education_level = education_mapping.get(education_level, 0)
    job_title_mapping = {
        "Software Engineer": 0,
        "Data Analyst": 1,
        "Senior Manager": 2,
        "Sales Associate": 3,
        "Director": 4,
        "Marketing Analyst": 5
    }
    job_title = job_title_mapping.get(job_title, 0)

    # Arrange features into a DataFrame with the correct feature names
    features = pd.DataFrame([[age, gender, education_level, job_title, years_of_experience]], 
                            columns=['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience'])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    # Format the prediction to 2 decimal places
    formatted_prediction = f"{prediction:,.2f}"
    
    return render_template('result.html', prediction_text=formatted_prediction)


if __name__ == "__main__":
    app.run(debug=True)
