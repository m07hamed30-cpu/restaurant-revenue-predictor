import streamlit as st
import pandas as pd
import joblib

# ---------- Page setup ----------
st.set_page_config(page_title="Restaurant Revenue Predictor", page_icon="🍽️", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #FAFAFA; }
        h1 { color: #D6336C; }
        .stButton>button {
            background-color: #D6336C;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover { background-color: #A61E4D; }
        .result-box {
            background-color: #FFF0F6;
            border: 2px solid #D6336C;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🍽️ Restaurant Revenue Predictor")
st.write("Estimate a restaurant's **expected monthly revenue** before investing, using a Machine Learning model trained on historical restaurant data.")

# ---------- Load the saved model, scaler and feature columns ----------
@st.cache_resource
def load_artifacts():
    model = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    return model, scaler, feature_columns

model, scaler, feature_columns = load_artifacts()

st.caption(f"Model in use: **{type(model).__name__}**  |  Trained R² ≈ 0.94")

st.divider()

# ---------- Input form ----------
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        customers = st.number_input("Number of Customers (monthly)", min_value=0, value=150)
        menu_price = st.number_input("Average Menu Price ($)", min_value=0.0, value=30.0)
        marketing_spend = st.number_input("Marketing Spend ($)", min_value=0.0, value=1200.0)
        avg_spending = st.number_input("Average Customer Spending ($)", min_value=0.0, value=35.0)

    with col2:
        seating_capacity = st.number_input("Seating Capacity", min_value=0, value=80)
        reviews = st.number_input("Number of Reviews", min_value=0, value=200)
        promotions = st.selectbox("Running Promotions?", ["Yes", "No"])
        cuisine = st.selectbox("Cuisine Type", ["American", "Italian", "Japanese", "Mexican", "Indian"])

    submitted = st.form_submit_button("Predict Revenue")

# ---------- Prediction ----------
if submitted:
    input_dict = {
        "Number_of_Customers": customers,
        "Menu_Price": menu_price,
        "Marketing_Spend": marketing_spend,
        "Average_Customer_Spending": avg_spending,
        "Seating_Capacity": seating_capacity,
        "Promotions": 1 if promotions == "Yes" else 0,
        "Reviews": reviews,
        "Customers_x_Spending": customers * avg_spending,
        "Cuisine_Type_Indian": 1 if cuisine == "Indian" else 0,
        "Cuisine_Type_Italian": 1 if cuisine == "Italian" else 0,
        "Cuisine_Type_Japanese": 1 if cuisine == "Japanese" else 0,
        "Cuisine_Type_Mexican": 1 if cuisine == "Mexican" else 0,
    }

    input_df = pd.DataFrame([input_dict], columns=feature_columns)
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.markdown(f"""
        <div class="result-box">
            <h3>Predicted Monthly Revenue</h3>
            <h1 style="color:#D6336C;">${prediction:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)
