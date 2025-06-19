import streamlit as st
import joblib

# Load the trained model
model = joblib.load('home_price_model.pkl')

st.title("🏠 Home Price Prediction App")

st.markdown("Enter the details below to predict the price of a house:")

# Input fields
area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=1500)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
age = st.number_input("Age of the House (in years)", min_value=0, max_value=100, value=10)

# Prediction
if st.button("Predict Price"):
    input_data = [[area, bedrooms, age]]
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated Home Price: ₹{prediction[0]:,.2f}")
