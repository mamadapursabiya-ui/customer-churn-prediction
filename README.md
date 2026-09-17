# 📊 Customer Churn Prediction & Retention System

A Machine Learning based web application that predicts whether a customer is likely to churn and provides retention recommendations.

---

# 🚀 Project Overview

Customer churn is a major challenge for businesses because losing existing customers can directly affect revenue.

This project uses **Machine Learning** to analyze customer information such as tenure, contract type, monthly charges, internet services, payment method, and other customer details to predict the probability of customer churn.

The prediction is presented through an interactive **Streamlit web application**.

---

# 🎯 Objectives

* Predict whether a customer is likely to churn
* Calculate the customer's churn probability
* Identify potential customer risk factors
* Provide retention recommendations
* Build an interactive and user-friendly ML application

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Streamlit**
* **Machine Learning**
* **Data Preprocessing**
* **Data Analysis**

---

# 🤖 Machine Learning

The project uses classification algorithms to predict customer churn.

### 📌 Models Used

* **Logistic Regression**
* **Random Forest Classifier**

The models are trained and evaluated, and the model with the better **ROC-AUC score** is selected.

---

# ⚙️ Data Preprocessing

The following preprocessing steps are performed:

* Remove unnecessary `customerID`
* Convert `TotalCharges` into numeric format
* Handle missing values
* One-Hot Encoding for categorical features
* Standard Scaling for numerical features
* Train-test split using stratification

---

# 📈 Model Evaluation

The models are evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1 Score**
* **ROC-AUC**
* **Confusion Matrix**

ROC-AUC is used to compare the model's ability to distinguish between customers who are likely to churn and those who are not.

---

# 💻 Application Features

## 🔹 Customer Information

Users can enter customer information including:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

---

# 📊 Churn Prediction

The application predicts whether the customer is:

**Likely to Churn**

or

**Unlikely to Churn**

It also displays the estimated **churn probability**.

---

# ⚠️ Customer Risk Level

The application categorizes customers into:

* 🟢 **Low Risk**
* 🟡 **Medium Risk**
* 🔴 **High Risk**

---

# 💡 Retention Recommendations

Based on customer information and identified risk factors, the application provides possible business actions such as:

* Offer suitable contract plans
* Provide discounts or incentives
* Improve technical support
* Recommend additional services
* Encourage long-term contracts

---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

The dataset and trained model are excluded from GitHub using `.gitignore`.

---

# 📊 Dataset

This project uses the **Telco Customer Churn Dataset**, containing customer demographic information, services, contract details, billing information, and churn status.

The dataset contains **7,043 customer records**.

---

# ▶️ How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/mamadapursabiya-ui/customer-churn-prediction.git
```

## 2️⃣ Open the Project

```bash
cd customer-churn-prediction
```

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4️⃣ Add the Dataset

Place the dataset inside the project folder with the filename:

```text
customer_churn.csv
```

## 5️⃣ Train the Model

```bash
python train_model.py
```

This creates:

```text
churn_model.pkl
```

## 6️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🔄 Project Workflow

```text
Customer Data
      ↓
Data Preprocessing
      ↓
Feature Encoding & Scaling
      ↓
Train ML Models
      ↓
Model Evaluation
      ↓
Select Best Model
      ↓
Save Trained Model
      ↓
Streamlit Application
      ↓
Customer Churn Prediction
      ↓
Risk Level
      ↓
Retention Recommendations
```

---

# 🌟 Key Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing
* Exploratory data analysis
* Classification algorithms
* Model evaluation
* Machine Learning pipelines
* Feature encoding
* Feature scaling
* Model comparison
* Model serialization using Joblib
* Streamlit application development
* Business-oriented Machine Learning

---

# 👩‍💻 Author

## **Sabiya Nazeerahmad Mamadapur**

**BE Computer Science & Engineering**

**Interests:** Data Science | Machine Learning | Python | Data Analytics

---

# ⭐ Project

If you find this project useful, feel free to explore the repository and provide feedback.
