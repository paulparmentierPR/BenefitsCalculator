import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title and Introduction
st.title("EASY24 Efficiency Calculator")
st.write("Make strategic decisions backed by data. Understand your potential savings and growth opportunities by shifting orders to our platform.")

# Input Metrics
st.subheader("Input Metrics")

col1, col2 = st.columns(2)
with col1:
    annual_orders = st.number_input("Enter Annual Order Volume:", value=1000000, step=1000)
with col2:
    percent_orders_easy24 = st.number_input("Enter % of Orders Going Through EASY24:", value=20.0, step=0.1) / 100
col3, col4 = st.columns(2)
with col3:
    sales_reps = st.number_input("Enter Sales Force Size:", value=40, step=1)
with col4:
    annual_cost_per_rep = st.number_input("Enter Annual Cost per Sales Rep (in €):", value=50000, step=1000)

# Calculations
orders_reduced = annual_orders * percent_orders_easy24
direct_cost_savings = annual_cost_per_rep * sales_reps * percent_orders_easy24

# Summary Box
st.subheader("Summary")
st.write(f"**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,} ({percent_orders_easy24 * 100:.1f}%)")

# Output Metrics
st.subheader("Strategic Insights")

# Waterfall Charts
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax1, ax2 = axes

# Order Reduction Waterfall
labels1 = ['Baseline', 'Reduction', 'Remaining']
values1 = [annual_orders, -orders_reduced, annual_orders - orders_reduced]
ax1.bar(labels1, np.cumsum(values1), color=['blue', 'green', 'blue'])
for i, (value, cum_value) in enumerate(zip(values1, np.cumsum(values1))):
    ax1.text(i, cum_value, f"{value:,}\n({cum_value:,})", ha='center', va='bottom')

# Monetary Savings Waterfall
labels2 = ['Baseline', 'Reduction', 'Remaining']
values2 = [annual_cost_per_rep * sales_reps, -direct_cost_savings, (annual_cost_per_rep * sales_reps) - direct_cost_savings]
ax2.bar(labels2, np.cumsum(values2), color=['blue', 'green', 'blue'])
for i, (value, cum_value) in enumerate(zip(values2, np.cumsum(values2))):
    ax2.text(i, cum_value, f"€{value:,}\n({(value / (annual_cost_per_rep * sales_reps) * 100):.1f}%)\n€{cum_value:,}", ha='center', va='bottom')

st.pyplot(fig)
