import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add custom font styling using st.markdown
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Start of the dashboard components
st.title("NavaFleet ROI Dashboard")
st.image("navagis_logo.jpeg", use_container_width=True)
st.sidebar.header("Input Metrics")
st.markdown("""
    <style>
    .header {
        color: #d32f2f;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    <div class="header">Welcome to the Navagis App</div>
""", unsafe_allow_html=True)

# Sidebar and input handling
vehicles_used = st.sidebar.number_input("Vehicles Used", min_value=1, value=41)
total_duration = st.sidebar.number_input("Total Duration (Hours)", min_value=1, value=555)
stops_per_vehicle = st.sidebar.number_input("Stops per Vehicle", min_value=1, value=17)

# Example calculations or visualizations here
st.write("Your dashboard content goes here!")
