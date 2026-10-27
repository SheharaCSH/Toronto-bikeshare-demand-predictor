from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Toronto Bike Share Predictor", page_icon="🚲")

@st.cache_resource
def load_model():
    return joblib.load(Path(__file__).parent / "models" / "best_model.joblib")

model = load_model()

st.title("🚲 Toronto Bike Share Demand Predictor")
st.write("Pick a day and the weather to predict how many rides Bike Share Toronto will see.")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

col1, col2 = st.columns(2)
with col1:
    temp = st.slider("Temperature (°C)", -20, 35, 15)
    rain = st.slider("Rain (mm)", 0.0, 50.0, 0.0)
    snow = st.slider("Snowfall (cm)", 0.0, 30.0, 0.0)
with col2:
    wind = st.slider("Max wind (km/h)", 0, 80, 15)
    weekday_name = st.selectbox("Day of week", DAYS)
    month = st.selectbox("Month", list(range(1, 13)), index=6)

weekday = DAYS.index(weekday_name)

row = pd.DataFrame([{
    "temp": temp, "rain": rain, "snow": snow, "wind": wind,
    "weekday": weekday, "month": month, "is_weekend": int(weekday >= 5),
}])

prediction = int(round(model.predict(row)[0]))
st.metric("Predicted rides", f"{prediction:,}")