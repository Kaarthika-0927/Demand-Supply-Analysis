import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Telangana Clothing Demand & Supply", layout="wide")

# Title
st.title("🧥 Telangana Clothing Demand vs Supply Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV
    df = pd.read_csv(uploaded_file)

    # Calculate surplus/shortage
    df["Status"] = df["Supply"] - df["Demand"]
    df["Condition"] = df["Status"].apply(lambda x: "Surplus" if x >= 0 else "Shortage")

    # Line plot: Demand vs Supply
    st.subheader("📊 Monthly Demand vs Supply")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df["Month"], df["Demand"], marker='o', label="Demand")
    ax1.plot(df["Month"], df["Supply"], marker='o', label="Supply")
    ax1.set_title("Monthly Demand vs Supply of Clothes in Telangana")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Number of Clothes")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

    # Bar chart: Surplus/Shortage
    st.subheader("📉 Surplus or Shortage Overview")
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    colors = df["Condition"].map({"Surplus": "green", "Shortage": "red"})
    ax2.bar(df["Month"], df["Status"], color=colors)
    ax2.axhline(0, color='black', linewidth=0.8)
    ax2.set_title("Monthly Surplus (+) or Shortage (-) of Clothes in Telangana")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Supply - Demand")
    st.pyplot(fig2)

    # Show data summary
    st.subheader("📝 Monthly Report Data")
    st.dataframe(df)

else:
    st.warning("Please upload the `telangana_clothing_demand_supply.csv` file to view the dashboard.")
