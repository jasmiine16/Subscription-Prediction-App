import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open("subscription_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🛍️ Subscription Prediction App")
st.write("Fill in the customer details to predict if they will subscribe.")

# Input fields for all features used during training (excluding Customer ID, Purchase Amount, and Subscription Status)
age = st.slider("Age", 18, 70, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
item_purchased = st.selectbox("Item Purchased", ["Laptop", "Shirt", "Novel", "Sofa", "Lipstick"])
category = st.selectbox("Category", ["Electronics", "Clothing", "Books", "Home", "Beauty"])
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
size = st.selectbox("Size", ["S", "M", "L", "XL"])
color = st.selectbox("Color", ["Red", "Blue", "Green", "Black", "White"])
season = st.selectbox("Season", ["Spring", "Summer", "Fall", "Winter"])
review_rating = st.slider("Review Rating", 1.0, 5.0, 4.0)
shipping_type = st.selectbox("Shipping Type", ["Standard", "Express", "Same Day"])
discount_applied = st.selectbox("Discount Applied", ["Yes", "No"])
promo_code_used = st.selectbox("Promo Code Used", ["Yes", "No"])
previous_purchases = st.number_input("Previous Purchases", min_value=0, value=1)
payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "PayPal", "Cash"])
frequency_of_purchases = st.slider("Frequency of Purchases", 0, 100, 10)

# Encoding inputs
gender_encoded = 1 if gender == "Male" else 0
item_encoded = {"Laptop": 0, "Shirt": 1, "Novel": 2, "Sofa": 3, "Lipstick": 4}[item_purchased]
category_encoded = {"Electronics": 0, "Clothing": 1, "Books": 2, "Home": 3, "Beauty": 4}[category]
location_encoded = {"Urban": 0, "Suburban": 1, "Rural": 2}[location]
size_encoded = {"S": 0, "M": 1, "L": 2, "XL": 3}[size]
color_encoded = {"Red": 0, "Blue": 1, "Green": 2, "Black": 3, "White": 4}[color]
season_encoded = {"Spring": 0, "Summer": 1, "Fall": 2, "Winter": 3}[season]
shipping_encoded = {"Standard": 0, "Express": 1, "Same Day": 2}[shipping_type]
discount_encoded = 1 if discount_applied == "Yes" else 0
promo_encoded = 1 if promo_code_used == "Yes" else 0
payment_encoded = {"Credit Card": 0, "Debit Card": 1, "PayPal": 2, "Cash": 3}[payment_method]

# Create input DataFrame
input_data = pd.DataFrame([{
    "Age": age,
    "Gender": gender_encoded,
    "Item Purchased": item_encoded,
    "Category": category_encoded,
    "Location": location_encoded,
    "Size": size_encoded,
    "Color": color_encoded,
    "Season": season_encoded,
    "Review Rating": review_rating,
    "Shipping Type": shipping_encoded,
    "Discount Applied": discount_encoded,
    "Promo Code Used": promo_encoded,
    "Previous Purchases": previous_purchases,
    "Payment Method": payment_encoded,
    "Frequency of Purchases": frequency_of_purchases
}])

# Prediction
if st.button("Predict Subscription Status"):
    prediction = model.predict(input_data)[0]
    result = "✅ Subscribed" if prediction == 1 else "❌ Not Subscribed"
    st.success(f"Prediction: {result}")
