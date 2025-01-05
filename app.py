import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('RFModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load teams from teams.pkl
with open('teams.pkl', 'rb') as teams_file:
    teams = pickle.load(teams_file)

# Load cities from city.pkl
with open('city.pkl', 'rb') as city_file:
    cities = pickle.load(city_file)

# Streamlit app title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Cricket Match Prediction App</h1>", unsafe_allow_html=True)

# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .stSelectbox, .stNumberInput, .stSlider {
        background-color: #e0f7fa;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Input fields
st.header("Input Match Details")

# Create two columns for side-by-side input fields
col1, col2 = st.columns(2)

# Batting and Bowling Teams (Side by side)
with col1:
    batting_team = st.selectbox("Batting Team", teams)

with col2:
    bowling_team = st.selectbox("Bowling Team", teams)

# City input
col3, col4 = st.columns(2)
with col3:
    city = st.selectbox("City", cities)

# Numeric Inputs in the columns
with col4:
    runs_left = st.number_input("Runs Left", min_value=0, step=1)

# Create another row of columns for additional inputs
col5, col6 = st.columns(2)
with col5:
    balls_left = st.number_input("Balls Left", min_value=0, step=1)

with col6:
    wickets = st.slider("Wickets Left", min_value=0, max_value=10, step=1)

col7, col8 = st.columns(2)
with col7:
    total_runs_x = st.number_input("Total Runs Target", min_value=0, step=1)

with col8:
    crr = st.number_input("Current Run Rate (CRR)", min_value=0.0, format="%.2f")

col9, col10 = st.columns(2)
with col9:
    rrr = st.number_input("Required Run Rate (RRR)", min_value=0.0, format="%.2f")

# Prediction button
if st.button("Predict"):
    # Create a DataFrame for the input
    input_data = pd.DataFrame(
        {
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [city],
            "runs_left": [runs_left],
            "balls_left": [balls_left],
            "wickets": [wickets],
            "total_runs_x": [total_runs_x],
            "crr": [crr],
            "rrr": [rrr],
        }
    )

    # Make prediction using the loaded model
    try:
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)  # Get class probabilities (if available)

        # Display prediction and class probabilities
        st.write(f"Prediction: {prediction[0]}")
        st.write(f"Probability of Class lose (0): {prediction_proba[0][0]:.2f}")
        st.write(f"Probability of Class win (1): {prediction_proba[0][1]:.2f}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
