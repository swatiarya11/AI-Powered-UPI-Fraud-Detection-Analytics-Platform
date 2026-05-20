# 🚨 AI-Powered UPI Fraud Detection & Analytics Platform

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-red?logo=streamlit)](https://ai-powered-upi-fraud-detection-system.streamlit.app/)

---

# 🌐 Live Web Application

👉 https://ai-powered-upi-fraud-detection-system.streamlit.app/

---

# 📌 Project Overview

The **AI-Powered UPI Fraud Detection & Analytics Platform** is an end-to-end Machine Learning project developed to detect fraudulent UPI transactions in real time.

This project combines:

- Data Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning
- Fraud Analytics
- Interactive Dashboards
- Web Application Deployment

The solution helps banks, fintech companies, and digital payment platforms identify suspicious transactions and minimize fraud risk using predictive analytics.

---

# 🚀 Key Features

- 🔍 Real-Time Fraud Prediction
- 📊 Interactive EDA Dashboard
- 📂 Batch Fraud Detection
- ☁️ Streamlit Cloud Deployment
- 📈 Fraud Trend Visualization
- 🔐 Login Authentication System
- 🤖 ML-Based Fraud Risk Scoring

---

# 🎯 Project Objectives

- Detect fraudulent UPI transactions using Machine Learning
- Perform fraud trend analysis and visualization
- Build an interactive EDA dashboard
- Create a real-time fraud prediction system
- Enable batch fraud detection through CSV upload
- Deploy the application using Streamlit Cloud

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| XGBoost | Fraud Prediction Model |
| Streamlit | Web Application |
| Plotly | Interactive Visualizations |
| SQL | Fraud Analysis Queries |
| Databricks | Data Cleaning & Processing |
| Power BI | Dashboard Visualization |
| GitHub | Version Control |

---

# 📈 Model Performance

| Metric | Score |
|---|---|
| Accuracy | 91.8% |
| ROC-AUC Score | 0.53 |
| Precision | 0.07 |
| Recall | 0.12 |
| F1-Score | 0.09 |

### Key Observation

XGBoost achieved the most balanced fraud detection performance under highly imbalanced fraud data conditions.

---

# 📂 Project Structure

```bash
AI-UPI-Fraud-Detection/
│
├── Data/
│   ├── raw_dataset.csv
│   ├── processed_dataset.csv
│
├── Databricks_Notebooks/
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── model_training.ipynb
│
├── SQL/
│   ├── fraud_analysis.sql
│
├── PowerBI/
│   ├── UPI_Fraud_Dashboard.pbix
│
├── Streamlit_WebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── xgb_fraud_model.pkl
│   ├── upi_transactions.csv
│
├── Presentation/
│   ├── Final_Presentation.pptx
│
├── Screenshots/
│   ├── home_dashboard.png
│   ├── eda_dashboard.png
│   ├── fraud_prediction.png
│   ├── batch_upload.png
│
├── README.md
```

---

# 📊 Dataset Information

The dataset contains transaction-related information such as:

- Transaction Amount
- Transaction Velocity
- Failed PIN Attempts
- Device Type
- Payment Application
- Merchant Information
- Weekend/Night Transactions
- User Risk Indicators

### Target Variable

- `is_fraud`
  - 0 → Genuine Transaction
  - 1 → Fraudulent Transaction

### Dataset Summary

| Attribute | Value |
|---|---|
| Total Transactions | 20,000+ |
| Fraud Rate | 3.82% |
| Domain | FinTech / Digital Payments |
| Time Period | Jan 2024 – Dec 2024 |

---

# 🤖 Machine Learning Model

## Model Used
- XGBoost Classifier

## Why XGBoost?

- Handles imbalanced datasets effectively
- High fraud prediction performance
- Fast prediction speed
- Better feature importance analysis
- Robust against overfitting

---

# 📊 Exploratory Data Analysis (EDA)

The EDA dashboard includes:

- Fraud Distribution Analysis
- Fraud by Payment App
- Fraud by Device Type
- Fraud by Transaction Type
- Monthly Fraud Trend
- High Risk User Analysis

### Key Insights

- Fraud transactions increased during weekends and late-night hours.
- Android devices showed higher fraud occurrence.
- Transaction velocity strongly influenced fraud probability.
- GPay and PhonePe showed higher fraud transaction counts.

---

# 🔍 Fraud Detection Parameters

The fraud prediction system analyzes:

- Transaction Amount
- Transaction Velocity
- Failed Attempts
- Recurring Payment Patterns
- Merchant Registration Status
- Weekend Transactions

---

# 📂 Batch Fraud Detection

The application supports CSV-based batch fraud prediction.

### Features

- Upload CSV transaction files
- Detect fraud transactions in bulk
- Generate fraud probability scores
- Download prediction results instantly

---

# ☁️ Deployment

The web application is successfully deployed using Streamlit Cloud.

### Live Application

https://ai-powered-upi-fraud-detection-system.streamlit.app/

---


# ⚠️ Challenges Faced

- Highly imbalanced fraud dataset
- Feature mismatch during prediction
- Duplicate columns after dataset merging
- Low fraud recall during initial modeling
- Streamlit deployment issues

---

# 🚀 Future Enhancements

- Real-time fraud monitoring APIs
- Deep Learning-based anomaly detection
- Live streaming dashboards
- Automated SMS/Email fraud alerts
- User registration system
- Cloud database integration

---

# 💼 Business Impact

- Improved fraud monitoring capability
- Faster suspicious transaction detection
- Reduced financial risk exposure
- Better data-driven decision making
- Enhanced transaction security analytics

---

# ✅ Conclusion

This project successfully demonstrates how Machine Learning, analytics, and interactive dashboards can be combined to detect fraudulent UPI transactions efficiently.

The solution provides:

- Real-time fraud prediction
- Fraud analytics dashboards
- Batch fraud analysis
- Cloud-based deployment
- Interactive visualization capabilities

The platform supports proactive fraud monitoring and intelligent decision-making for digital payment systems.

---

# 👩‍💻 Author

# _Swati Arya_
