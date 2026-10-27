# 🚲 Toronto Bike Share Demand Predictor

A machine learning web app that predicts daily Bike Share Toronto ridership from weather and calendar data.

**🔗 Live demo:** https://toronto-bikeshare-demand-predictor-7co4y9zzatcmavjgve4euy.streamlit.app/

## What it does
Pick a temperature, rain, snowfall, wind speed, day of the week, and month, and the app predicts how many rides Bike Share Toronto will see that day.

## Data
- **Rides:** Bike Share Toronto 2024 ridership data (Toronto Open Data), about 5 million trips aggregated to daily counts.
- **Weather:** Daily Toronto weather from the Open-Meteo archive API.

## Approach
1. Aggregated trips into 366 daily ride counts and merged them with weather.
2. Added calendar features (weekday, month, weekend flag).
3. Explored the data. Rides rise strongly with temperature, peak July to September, and drop on rainy days.
4. Trained Linear Regression and Random Forest models and compared them.
5. Served the best model through a FastAPI endpoint and a Streamlit app.

## Results
| Model | MAE (rides/day) | R² |
|---|---|---|
| Linear Regression | 2,829 | 0.84 |
| **Random Forest** | **2,483** | **0.89** |

Evaluated on a random 20% test split.

## Limitations
Only one year of data was used, so the model cannot capture year-over-year growth. Next steps are adding 2022 to 2025 data and testing on a time-based split.

## Tech stack
Python, pandas, scikit-learn, FastAPI, Streamlit, Jupyter, Git

## Run it locally
```
git clone https://github.com/SheharaCSH/Toronto-bikeshare-demand-predictor.git
cd Toronto-bikeshare-demand-predictor
pip install -r requirements.txt
streamlit run app.py
```

To rebuild the data, download the 2024 ridership file from Toronto Open Data into `data/`, then run `python get_weather.py` and `notebooks/01_data_prep.ipynb`.

## Author
Chamudi Shehara Hennayaka, Software Engineering Technology (AI), Centennial College