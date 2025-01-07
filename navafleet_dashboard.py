
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




def calculate_navafleet_metrics(vehicles_used, total_duration, stops_per_vehicle):
    improvements = {
        "vehicles_used_reduction": 51,
        "total_duration_reduction": 43,
        "stops_per_vehicle_increase": 100
    }
    
    navafleet_metrics = {
        "vehicles_used": vehicles_used * (1 - improvements["vehicles_used_reduction"] / 100),
        "total_duration": total_duration * (1 - improvements["total_duration_reduction"] / 100),
        "stops_per_vehicle": stops_per_vehicle * (1 + improvements["stops_per_vehicle_increase"] / 100)
    }
    
    return navafleet_metrics

def create_navafleet_dashboard():
    st.title("NavaFleet ROI Dashboard")
    st.image("navagis_logo.jpeg", use_column_width=True)
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
    st.markdown("""
    <style>
    .css-1d391kg {  # This targets Streamlit's sidebar
        background-color: #f1f1f1;
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

    vehicles_used = st.sidebar.number_input("Vehicles Used", min_value=1, value=41)
    total_duration = st.sidebar.number_input("Total Duration (Hours)", min_value=1, value=555)
    stops_per_vehicle = st.sidebar.number_input("Stops per Vehicle", min_value=1, value=17)
    
    navafleet_metrics = calculate_navafleet_metrics(vehicles_used, total_duration, stops_per_vehicle)
    
    st.header("Comparison of Metrics")
    
    st.write("### Current System vs NavaFleet")
    st.write(f"- **Vehicles Used**: {vehicles_used:.2f} ➡️ {navafleet_metrics['vehicles_used']:.2f}")
    st.write(f"- **Total Duration (Hours)**: {total_duration:.2f} ➡️ {navafleet_metrics['total_duration']:.2f}")
    st.write(f"- **Stops per Vehicle**: {stops_per_vehicle:.2f} ➡️ {navafleet_metrics['stops_per_vehicle']:.2f}")
    
    st.write("### Key Improvements with NavaFleet")
    st.write("- **51% Reduction** in fleet vehicles needed")
    st.write("- **43% Reduction** in total duration")
    st.write("- **100% Increase** in stops per vehicle")
    
    metrics_data = pd.DataFrame({
        "Metric": ["Vehicles Used", "Total Duration (Hours)", "Stops per Vehicle"],
        "Current System": [vehicles_used, total_duration, stops_per_vehicle],
        "NavaFleet": [
            navafleet_metrics["vehicles_used"],
            navafleet_metrics["total_duration"],
            navafleet_metrics["stops_per_vehicle"]
        ]
    })

    st.write("### Visual Comparison of Metrics")
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_chart = metrics_data.plot(kind="bar", x="Metric", ax=ax)
    
    # Annotating the chart with percentage changes
    for index, row in metrics_data.iterrows():
        metric = row["Metric"]
        current = row["Current System"]
        navafleet = row["NavaFleet"]
        change = ((navafleet - current) / current) * 100
        
        # Set annotation color dynamically
        color = "green" if change > 0 else "red"
        
        # Annotate above NavaFleet bar
        ax.annotate(
            f"{change:+.1f}%",
            (index + 0.15, navafleet + navafleet * 0.05),  # Adjusted x and y for clarity
            color=color,  # Dynamic color
            fontsize=10,
            ha="center"
        )

    ax.set_ylabel("Value")
    ax.set_title("Metrics Comparison")
    plt.xticks(rotation=0)
    st.pyplot(fig)
create_navafleet_dashboard()
