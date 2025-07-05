import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("carbon_model.pkl", "rb"))

st.title("🌍 CO₂ Emission Predictor")
st.markdown("Predicting CO₂ Emissions")

year = st.slider("Year", 1990, 2050, 2025)
gdp = st.number_input("GDP (in trillions)", value=5.0, step=1.0, format="%.2f") * 1e12
en_per_cap = st.slider("Energy Use per Capita", 200, 10000, 550)
pop = st.number_input("Population", value=7_000_000, step=100_000)
urb_pop = st.number_input("Urban Population", value=2_000_000, step=100_000)

if st.button("Predict"):
    input_data = pd.DataFrame([[
        year, gdp, en_per_cap, pop, urb_pop
    ]], columns=[
        "year", "gdp", "en_per_cap", "pop", "urb_pop"
    ])
    prediction = model.predict(input_data)[0]
    st.info(f"🌱 Estimated CO₂ Emission: **{prediction:,.2f} metric tons**")

    if prediction > 250000: # as of now co2 is already high so this number will be nearly safe
      st.error("🚨 Estimated CO₂ Emissions exceed the global danger threshold (25 billion metric tons)!")
      st.markdown("### 🌡️ CO₂ Status: **Danger Zone**")
    else:
      st.success("Estimated CO₂ emissions are within the safe limit.")
      st.markdown("### CO₂ Status: **Acceptable Range**")

    
    

