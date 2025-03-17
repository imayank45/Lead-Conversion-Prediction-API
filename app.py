# app.py
from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('models/model_rf2.pkl', 'rb') as file:
    model = pickle.load(file)

# Assuming these are the features your model was trained on
FEATURES = ['Age', 'Gender', 'Location', 'LeadSource', 'TimeSpent (minutes)', 
           'PagesViewed', 'LeadStatus', 'EmailSent', 'DeviceType', 'ReferralSource',
           'FormSubmissions', 'Downloads', 'CTR_ProductPage', 'ResponseTime (hours)',
           'FollowUpEmails', 'SocialMediaEngagement', 'PaymentHistory']

# Preprocessing function (adjust based on your model's training preprocessing)
def preprocess_input(data):
    df = pd.DataFrame([data])
    
    # Convert categorical variables to numeric (simple encoding - adjust as per your model)
    categorical_mappings = {
        'Gender': {'Male': 0, 'Female': 1},
        'Location': {'Lahore': 0, 'Sialkot': 1, 'Quetta': 2},
        'LeadSource': {'Organic': 0, 'Email': 1},
        'LeadStatus': {'Cold': 0, 'Warm': 1, 'Hot': 2},
        'DeviceType': {'Mobile': 0, 'Tablet': 1, 'Desktop': 2},
        'ReferralSource': {'Facebook': 0, 'Direct': 1},
        'PaymentHistory': {'No Payment': 0, 'Good': 1}
    }
    
    for col, mapping in categorical_mappings.items():
        df[col] = df[col].map(mapping)
    
    return df[FEATURES]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'Age': float(request.form['Age']),
                'Gender': request.form['Gender'],
                'Location': request.form['Location'],
                'LeadSource': request.form['LeadSource'],
                'TimeSpent (minutes)': float(request.form['TimeSpent']),
                'PagesViewed': float(request.form['PagesViewed']),
                'LeadStatus': request.form['LeadStatus'],
                'EmailSent': float(request.form['EmailSent']),
                'DeviceType': request.form['DeviceType'],
                'ReferralSource': request.form['ReferralSource'],
                'FormSubmissions': float(request.form['FormSubmissions']),
                'Downloads': float(request.form['Downloads']),
                'CTR_ProductPage': float(request.form['CTR_ProductPage']),
                'ResponseTime (hours)': float(request.form['ResponseTime']),
                'FollowUpEmails': float(request.form['FollowUpEmails']),
                'SocialMediaEngagement': float(request.form['SocialMediaEngagement']),
                'PaymentHistory': request.form['PaymentHistory']
            }
            
            # Preprocess the input
            processed_data = preprocess_input(data)
            
            # Make prediction
            probability = model.predict_proba(processed_data)[0][1]
            
            return render_template('index.html', 
                                 prediction=f"{probability*100:.2f}%",
                                 success=True)
        except Exception as e:
            return render_template('index.html', 
                                 error=f"Error: {str(e)}",
                                 success=False)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)