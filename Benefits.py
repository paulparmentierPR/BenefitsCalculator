import streamlit as st
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Efficiency Calculator")
st.write("Make strategic decisions backed by data. Understand your potential savings and growth opportunities by shifting orders to our platform.")

# Input Metrics
st.subheader("Input Metrics")
annual_orders = st.number_input("Enter Annual Order Volume:", value=1000000, step=1000)
sales_reps = st.number_input("Enter Sales Force Size:", value=40, step=1)
annual_cost_per_rep = st.number_input("Enter Annual Cost per Sales Rep (in €):", value=50000, step=1000)
percent_orders_easy24 = st.number_input("Enter % of Orders Going Through EASY24:", value=20.0, step=0.1) / 100

# Calculations
orders_reduced = annual_orders * percent_orders_easy24
direct_cost_savings = annual_cost_per_rep * sales_reps * percent_orders_easy24

# Summary Box
st.subheader("Summary")
st.write(f"**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,}")

# Output Metrics
st.subheader(f"Strategic Insights for {annual_orders:,} Orders & {sales_reps} Sales Reps")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Fixed the issue here

# ... Rest of the code remains the same
