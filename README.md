📊 Customer Churn Prediction & Retention System

A Machine Learning based web application that predicts whether a customer is likely to churn and provides personalized retention recommendations.

🚀 Project Overview

Customer churn is a major challenge for businesses because losing existing customers can directly affect revenue.

This project uses Machine Learning to analyze customer information such as tenure, contract type, monthly charges, internet services, payment method, and other customer details to predict the probability of customer churn.

The prediction is presented through an interactive Streamlit web application.

🎯 Objectives
Predict whether a customer is likely to churn.
Calculate the customer's churn probability.
Identify potential risk factors.
Provide business-oriented retention recommendations.
Build an easy-to-use interactive dashboard.
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Machine Learning
Data Preprocessing
Data Analysis
🤖 Machine Learning

The project compares different classification algorithms:

Logistic Regression
Random Forest Classifier
Data Preprocessing

The following preprocessing techniques are used:

Handling missing values
Converting TotalCharges into numeric format
Removing unnecessary customerID
One-Hot Encoding for categorical features
Standard Scaling for numerical features
Train-test split with stratification
Evaluation Metrics

The models are evaluated using:

Accuracy
Precision
Recall
F1 Score
ROC-AUC
Confusion Matrix

The model with the better ROC-AUC score is selected and saved using Joblib.

💻 Application Features
Customer Prediction

Users can enter customer information such as:

Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming Services
Contract
Paperless Billing
Payment Method
Monthly Charges
Total Charges
📈 Churn Probability

The application displays the estimated probability that a customer will churn.

⚠️ Risk Level

Customers are categorized into:

Low Risk
Medium Risk
High Risk
💡 Retention Recommendations

Based on customer information and identified risk factors, the application provides possible retention actions.

📂 Project Structure
customer-churn-prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md

The dataset and generated model file are excluded from the GitHub repository using .gitignore.

📊 Dataset

This project uses the Telco Customer Churn dataset, which contains customer demographic information, services, contract details, billing information, and churn status.

The dataset contains 7,043 customer records.

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/mamadapursabiya-ui/customer-churn-prediction.git
2. Open the project
cd customer-churn-prediction
3. Install the required libraries
pip install -r requirements.txt
4. Add the dataset

Place the dataset in the project folder with the filename:

customer_churn.csv
5. Train the model
python train_model.py

This will generate:

churn_model.pkl
6. Run the Streamlit application
streamlit run app.py

The application will open in your browser.

🔄 Project Workflow
Customer Data
      ↓
Data Preprocessing
      ↓
Feature Encoding & Scaling
      ↓
Train Multiple ML Models
      ↓
Model Evaluation
      ↓
Select Best Model
      ↓
Save Model
      ↓
Streamlit Web Application
      ↓
Churn Prediction
      ↓
Risk Level & Retention Recommendations
🌟 Key Learning Outcomes

Through this project, I worked with:

Data preprocessing
Feature engineering
Classification algorithms
Model evaluation
Machine Learning pipelines
Hyperparameter/model comparison
Model serialization using Joblib
Streamlit application development
Business-oriented ML predictions
