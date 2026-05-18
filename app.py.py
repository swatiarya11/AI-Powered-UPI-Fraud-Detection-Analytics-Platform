import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# =====================================
# LOGIN SYSTEM
# =====================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.set_page_config(
        page_title="UPI Fraud Detection Login",
        page_icon="🔐",
        layout="centered"
    )

    st.markdown("""
        <style>
        .main {
            background-color: #0E1117;
        }

        .login-box {
            background-color: #1c1f26;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        }

        h1, h2, h3 {
            color: white;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🔐 UPI Fraud Detection System</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class='login-box'>
    """, unsafe_allow_html=True)

    st.info("""
    ### Demo Login Credentials

    👤 Username: `admin`  
    🔑 Password: `admin123`
    """)

    username = st.text_input("Enter Username")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="UPI Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("xgb_fraud_model.pkl")

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stMetricValue"] {
    color: #00FFAA;
    font-size: 28px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("💳 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "📊 EDA Dashboard",
        "🔍 Fraud Prediction",
        "📂 Batch Upload"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.title("💳 UPI Fraud Detection System")

    st.subheader("AI-Powered Fraud Analytics Platform")

    st.markdown("""
    ### Welcome

    This web application helps banks and fintech companies detect fraudulent UPI transactions using Machine Learning.

    ### Key Features:
    ✅ Real-time Fraud Prediction  
    ✅ Exploratory Data Analysis  
    ✅ Fraud Risk Scoring  
    ✅ Transaction Monitoring  
    ✅ Fraud Trend Analysis  

    ---
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Transactions", "20K")
    col2.metric("Fraud Transactions", "763")
    col3.metric("Fraud Rate", "3.82%")
    col4.metric("High Risk Users", "5.35%")

    st.markdown("---")

    st.info("""
    Navigate to the EDA Dashboard for visual analysis
    and Fraud Prediction tab for real-time prediction.
    """)


# =====================================================
# EDA DASHBOARD
# =====================================================

elif page == "📊 EDA Dashboard":

    st.title("📊 Exploratory Data Analysis Dashboard")

    try:

        df = pd.read_csv("upi_transactions.csv.csv")

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        st.markdown("---")

        # KPI CARDS

        col1, col2, col3 = st.columns(3)

        total_txn = len(df)

        fraud_txn = df['is_fraud'].sum()

        fraud_rate = round((fraud_txn / total_txn) * 100, 2)

        col1.metric("Total Transactions", total_txn)
        col2.metric("Fraud Transactions", fraud_txn)
        col3.metric("Fraud Rate", f"{fraud_rate}%")

        st.markdown("---")

        # CHART 1

        st.subheader("Fraud by Payment App")

        app_fraud = df.groupby("payment_app")["is_fraud"].sum().reset_index()

        fig1 = px.bar(
            app_fraud,
            x="payment_app",
            y="is_fraud",
            color="payment_app",
            title="Fraud Transactions by Payment App"
        )

        st.plotly_chart(fig1, use_container_width=True)

        # CHART 2

        st.subheader("Fraud vs Genuine Transactions")

        fraud_counts = df['is_fraud'].value_counts()

        fig2 = px.pie(
            values=fraud_counts.values,
            names=["Genuine", "Fraud"],
            title="Fraud Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)

        # CHART 3

        st.subheader("Fraud by Transaction Type")

        txn_type = df.groupby("transaction_type")["is_fraud"].sum().reset_index()

        fig3 = px.bar(
            txn_type,
            x="transaction_type",
            y="is_fraud",
            color="transaction_type",
            title="Fraud by Transaction Type"
        )

        st.plotly_chart(fig3, use_container_width=True)

        # CHART 4

        st.subheader("Fraud by Device Type")

        device = df.groupby("device_type")["is_fraud"].sum().reset_index()

        fig4 = px.bar(
            device,
            x="device_type",
            y="is_fraud",
            color="device_type",
            title="Fraud by Device Type"
        )

        st.plotly_chart(fig4, use_container_width=True)

        # CHART 5

        st.subheader("Fraud Trend Over Time")

        # CREATE MONTH COLUMN FROM DATE

        df['date'] = pd.to_datetime(df['date'])
        
        df['month'] = df['date'].dt.month_name()
        
        trend = df.groupby("month")["is_fraud"].sum().reset_index()
        
        fig5 = px.line(
            trend,
            x="month",
            y="is_fraud",
            markers=True,
            title="Monthly Fraud Trend"
        )
        
        st.plotly_chart(fig5, use_container_width=True)

    except Exception as e:

        st.error(e)

# =====================================================
# FRAUD PREDICTION
# =====================================================

elif page == "🔍 Fraud Prediction":

    st.title("🔍 Real-Time Fraud Prediction")

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    transaction_velocity = st.slider(
        "Transaction Velocity",
        1,
        10,
        3
    )

    failed_attempts = st.slider(
        "Failed Attempts Last 24H",
        0,
        10,
        1
    )

    is_weekend = st.selectbox(
        "Is Weekend?",
        [0, 1]
    )

    recurring_payment = st.selectbox(
        "Recurring Payment?",
        [0, 1]
    )

    is_registered = st.selectbox(
        "Is Registered Merchant?",
        [0, 1]
    )

    if st.button("Predict Fraud"):

        input_data = pd.DataFrame({

            'AMOUNT': [amount],

            'TRANSACTION_VELOCITY': [transaction_velocity],

            'FAILED_ATTEMPTS_LAST_24H': [failed_attempts],

            'IS_WEEKEND': [is_weekend],

            'RECURRING_PAYMENT_FLAG': [recurring_payment],

            'IS_REGISTERED': [is_registered]

        })

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        st.subheader("Prediction Result")

        st.metric(
            "Fraud Probability",
            f"{round(probability * 100, 2)}%"
        )

        if prediction == 1:
            st.error("🚨 Fraudulent Transaction Detected")
        else:
            st.success("✅ Genuine Transaction")

# =========================
# BATCH FRAUD DETECTION
# =========================

elif page == "📂 Batch Upload":

    st.title("📂 Batch Fraud Detection")

    st.markdown("""
    Upload a CSV file to detect fraudulent transactions in bulk.
    """)

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            batch_df = pd.read_csv(uploaded_file)

            st.subheader("Uploaded Dataset")

            st.dataframe(batch_df.head())

            # REQUIRED FEATURES

            required_cols = [
                'amount',
                'transaction_velocity',
                'failed_attempts_last_24h',
                'is_weekend',
                'recurring_payment_flag'
            ]

            missing_cols = [
                col for col in required_cols
                if col not in batch_df.columns
            ]

            if missing_cols:

                st.error(f"Missing columns: {missing_cols}")

            else:

                # CREATE MODEL INPUT

                input_data = pd.DataFrame({

                    'AMOUNT':
                    batch_df['amount'],

                    'TRANSACTION_VELOCITY':
                    batch_df['transaction_velocity'],

                    'FAILED_ATTEMPTS_LAST_24H':
                    batch_df['failed_attempts_last_24h'],

                    'IS_WEEKEND':
                    batch_df['is_weekend'],

                    'RECURRING_PAYMENT_FLAG':
                    batch_df['recurring_payment_flag'],

                    # GENERATED COLUMN
                    'IS_REGISTERED':
                    1

                })

                # PREDICTIONS

                prediction = model.predict(input_data)

                probability = (
                    model.predict_proba(input_data)[:,1]
                )

                batch_df['Prediction'] = prediction

                batch_df['Fraud_Probability (%)'] = (
                    probability * 100
                ).round(2)

                batch_df['Prediction_Label'] = (
                    batch_df['Prediction']
                    .map({
                        0: "Genuine",
                        1: "Fraud"
                    })
                )

                # METRICS

                fraud_count = (
                    batch_df['Prediction']
                    .sum()
                )

                genuine_count = (
                    len(batch_df) - fraud_count
                )

                col1, col2 = st.columns(2)

                col1.metric(
                    "Fraud Transactions",
                    fraud_count
                )

                col2.metric(
                    "Genuine Transactions",
                    genuine_count
                )

                st.markdown("---")

                st.subheader("Prediction Results")

                st.dataframe(batch_df.head(20))

                # DOWNLOAD BUTTON

                csv = batch_df.to_csv(index=False)

                st.download_button(
                    label="Download Results CSV",
                    data=csv,
                    file_name="fraud_predictions.csv",
                    mime="text/csv"
                )

        except Exception as e:

            st.error(f"Error: {e}")

