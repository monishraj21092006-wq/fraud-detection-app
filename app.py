import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

st.title("🛡️ AI Fraud Detection System")

# Input
login_hour = st.sidebar.slider("Login Hour", 0, 23, 10)
transactions = st.sidebar.slider("Transactions", 1, 50, 5)
amount = st.sidebar.number_input("Amount", 100, 100000, 5000)
downloads = st.sidebar.slider("Downloads", 1, 1000, 50)

# Normal data
np.random.seed(42)
data = pd.DataFrame({
    "login_hour": np.random.normal(10, 2, 200),
    "transactions": np.random.normal(5, 2, 200),
    "amount": np.random.normal(5000, 2000, 200),
    "downloads": np.random.normal(50, 20, 200)
})

# Model
model = IsolationForest(contamination=0.05)
model.fit(data)

# Prediction
input_data = pd.DataFrame([[login_hour, transactions, amount, downloads]],
                          columns=data.columns)

prediction = model.predict(input_data)

# Risk Score
risk = 0
if login_hour < 6 or login_hour > 22:
    risk += 30
if transactions > 15:
    risk += 25
if amount > 30000:
    risk += 25
if downloads > 300:
    risk += 20

# Output
st.subheader("Result")

if prediction[0] == -1 or risk > 50:
    st.error("🚨 Fraud Detected!")
else:
    st.success("✅ Normal Activity")

st.write("Risk Score:", risk)