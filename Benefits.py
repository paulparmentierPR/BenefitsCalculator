import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title and Introduction
st.title("EASY24 Efficiency Calculator")
st.write("Make strategic decisions backed by data. Understand your potential savings and growth opportunities by shifting orders to our platform.")

# Summary Box
st.subheader("Summary")
orders_reduced = annual_orders * percent_orders_easy24
direct_cost_savings = annual_cost_per_rep * sales_reps * percent_orders_easy24
st.write(f"**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,}")

# Input Metrics
st.subheader("Input Metrics")
annual_orders = st.number_input("Enter Annual Order Volume:", value=1000000, step=1000)
sales_reps = st.number_input("Enter Sales Force Size:", value=40, step=1)
annual_cost_per_rep = st.number_input("Enter Annual Cost per Sales Rep (in €):", value=50000, step=1000)
percent_orders_easy24 = st.number_input("Enter % of Orders Going Through EASY24:", value=20.0, step=0.1) / 100

# Calculations
orders_reduced = annual_orders * percent_orders_easy24
direct_cost_savings = annual_cost_per_rep * sales_reps * percent_orders_easy24

# Output Metrics
st.subheader(f"Strategic Insights for {annual_orders:,} Orders & {sales_reps} Sales Reps")

# Waterfall Charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Orders Waterfall Chart
labels1 = ['Total Orders', 'Orders Reduced']
values1 = [annual_orders, -orders_reduced]
cumulative_values1 = np.cumsum(values1)
ax1.bar(labels1, cumulative_values1, color=['#1f77b4', '#2ca02c'])
ax1.set_title("Order Reduction")
for i, value in enumerate(cumulative_values1):
    ax1.text(i, value, str(round(values1[i], 2)), ha='center', va='bottom')

# Monetary Savings Waterfall Chart
labels2 = ['Baseline Cost (€)', 'Direct Cost Savings (€)']
values2 = [annual_cost_per_rep * sales_reps, -direct_cost_savings]
cumulative_values2 = np.cumsum(values2)
ax2.bar(labels2, cumulative_values2, color=['#1f77b4', '#2ca02c'])
ax2.set_title("Monetary Savings")
for i, value in enumerate(cumulative_values2):
    ax2.text(i, value, f"€{round(values2[i], 2)}\n({(values2[i]/(annual_cost_per_rep * sales_reps))*100:.1f}%)", ha='center', va='bottom')

st.pyplot(fig)
