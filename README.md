# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to **churn** or **stay**.

## 🚀 Project Overview

Customer churn occurs when a customer stops using a company's services.

This project uses customer information such as:

- Customer demographics
- Services used
- Contract type
- Tenure
- Monthly charges
- Total charges
- Payment method

to predict the likelihood of customer churn.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Logistic Regression
- One-Hot Encoding
- Streamlit

## 📊 Dataset

The project uses the **Telco Customer Churn dataset**.

The dataset contains customer information and a `Churn` column indicating whether a customer left the company.

## ⚙️ Machine Learning Workflow

```text
Customer Data
      ↓
Data Cleaning
      ↓
Categorical Encoding
      ↓
Train/Test Data
      ↓
Logistic Regression
      ↓
Churn Prediction
```

## 🤖 Machine Learning Model

The project uses **Logistic Regression** for binary classification.

Categorical features are converted into numerical features using **One-Hot Encoding**.

## ✨ Features

- Customer churn prediction
- Churn probability
- Customer information input
- Billing information input
- Interactive Streamlit interface
- Real-time prediction

## 💻 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── app.py
├── model.py
├── requirements.txt
└── README.md
```

## 👨‍💻 Author

Smit
```

### Bas itna hi. ✅

Phir **Ctrl + S** karo.

**Kuch aur add/delete mat karna.**