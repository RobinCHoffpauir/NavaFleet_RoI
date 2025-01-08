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
    # Navagis colors
    navagis_red = "#d32f2f"
    navagis_green = "#4caf50"
    navagis_blue = "#42a5f5"
    navagis_light_gray = "#f4f4f4"
    navagis_dark_gray = "#333333"

    # Inject custom font and global styling
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f4f4;  /* Light gray for a modern look */
            color: #333333;
        }

        section[data-testid="stSidebar"] {
            background-color: #e3f2fd; /* Light blue for sidebar */
        }

        .header {
            color: #d32f2f;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main dashboard title and logo
    st.title("NavaFleet ROI Dashboard")
    st.image("navagis_logo.jpeg", use_container_width=True)
    st.sidebar.header("Input Metrics")

    # Sidebar and input handling
    vehicles_used = st.sidebar.number_input("Vehicles Used", min_value=1, value=41)
    total_duration = st.sidebar.number_input("Total Duration (Hours)", min_value=1, max_value=700, value=555)
    stops_per_vehicle = st.sidebar.number_input("Stops per Vehicle", min_value=1, max_value=40, value=17)

    # Calculate metrics
    navafleet_metrics = calculate_navafleet_metrics(vehicles_used, total_duration, stops_per_vehicle)

    # Main content
    st.markdown('<div class="header">NavaFleet ROI Estimator</div>', unsafe_allow_html=True)
    st.header("Comparison of Metrics")
    st.write("### Current System vs NavaFleet")
    st.write(f"- **Vehicles Used**: {vehicles_used:.2f} ➡️ {navafleet_metrics['vehicles_used']:.2f}")
    st.write(f"- **Total Duration (Hours)**: {total_duration:.2f} ➡️ {navafleet_metrics['total_duration']:.2f}")
    st.write(f"- **Stops per Vehicle**: {stops_per_vehicle:.2f} ➡️ {navafleet_metrics['stops_per_vehicle']:.2f}")

    st.write("### Key Improvements with NavaFleet")
    st.write("- **51% Reduction** in fleet vehicles needed")
    st.write("- **43% Reduction** in total duration")
    st.write("- **100% Increase** in stops per vehicle")

    # Create a metrics comparison chart
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
    bar_chart = metrics_data.plot(kind="bar", x="Metric", ax=ax, color=[navagis_red, navagis_green])
    
    # Annotating the chart with percentage changes
    for index, row in metrics_data.iterrows():
        metric = row["Metric"]
        current = row["Current System"]
        navafleet = row["NavaFleet"]
        change = ((navafleet - current) / current) * 100

        color = navagis_green if change > 0 else navagis_red

        ax.annotate(
            f"{change:+.1f}%",
            (index + 0.15, navafleet + navafleet * 0.05),
            color=color,
            fontsize=10,
            ha="center"
        )

    ax.set_ylabel("Value")
    ax.set_title("Metrics Comparison")
    plt.xticks(rotation=0)
    st.pyplot(fig)

    # Disclaimer
    st.markdown("---")
    st.write("""
        **Disclaimer:**
        - This calculator provides an estimation of ROI based on the inputs you provide. 
        - The results are not guaranteed to reflect the exact performance or outcomes in your organization.
        - Real-world results may vary due to factors such as operational differences, market conditions, and unforeseen circumstances.
        - This tool is for informational purposes only and should not be considered financial or investment advice. Please consult with a qualified professional for specific recommendations tailored to your organization.
    """)

create_navafleet_dashboard()
