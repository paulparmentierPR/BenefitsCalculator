import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title and Introduction
st.title("EASY24 Efficiency Calculator")
st.write("Make strategic decisions backed by data. Understand your potential savings and growth opportunities by shifting orders to our platform.")

# Input Metrics
st.subheader("Input Metrics")
annual_orders = st.number_input("Enter Annual Order Volume:", value=1000000, step=1000)
sales_reps = st.number_input("Enter Sales Force Size:", value=40, step=1)
annual_cost_per_rep = st.number_input("Enter Annual Cost per Sales Rep (in €):", value=50000, step=1000)

# Calculations
orders_reduced = annual_orders * 0.2
direct_cost_savings = annual_cost_per_rep * sales_reps * 0.2

# Output Metrics
st.subheader(f"Strategic Insights for {annual_orders:,} Orders & {sales_reps} Sales Reps")

# First Waterfall Chart for Order Reduction
fig1, ax1 = plt.subplots()
labels1 = ['Total Orders', 'Orders Reduced', 'Remaining Orders']
values1 = [annual_orders, -orders_reduced, annual_orders - orders_reduced]
cumulative_values1 = np.cumsum(values1)
ax1.bar(labels1, cumulative_values1, color=['#1f77b4', '#d62728', '#2ca02c'])
ax1.set_title("Order Reduction Waterfall Chart")
for i, value in enumerate(cumulative_values1):
    ax1.text(i, value, str(round(values1[i], 2)), ha='center', va='bottom')
st.pyplot(fig1)

# Second Waterfall Chart for Monetary Savings
fig2, ax2 = plt.subplots()
labels2 = ['Baseline Cost (€)', 'Direct Cost Savings (€)', 'Final Cost (€)']
values2 = [annual_cost_per_rep * sales_reps, -direct_cost_savings, annual_cost_per_rep * sales_reps - direct_cost_savings]
cumulative_values2 = np.cumsum(values2)
ax2.bar(labels2, cumulative_values2, color=['#1f77b4', '#d62728', '#2ca02c'])
ax2.set_title("Monetary Savings Waterfall Chart")
for i, value in enumerate(cumulative_values2):
    ax2.text(i, value, str(round(values2[i], 2)), ha='center', va='bottom')
st.pyplot(fig2)

# Summary Box
st.subheader("Summary")
st.write(f"**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,}")
