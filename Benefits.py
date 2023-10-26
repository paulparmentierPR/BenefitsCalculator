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
baseline_cost = annual_cost_per_rep * sales_reps
orders_reduced = annual_orders * 0.2
direct_cost_savings = annual_cost_per_rep * sales_reps * 0.2
final_cost = baseline_cost - direct_cost_savings

# Output Metrics
st.subheader(f"Strategic Insights for {annual_orders:,} Orders & {sales_reps} Sales Reps")

# Waterfall Chart
labels = ['Baseline Cost (€)', 'Orders Reduced', 'Direct Cost Savings (€)', 'Final Cost (€)']
values = [baseline_cost, 0, -direct_cost_savings, final_cost]
cumulative_values = np.cumsum(values)

fig, ax = plt.subplots()
ax.bar(labels, cumulative_values, color=['#1f77b4', '#1f77b4', '#d62728', '#2ca02c'])
ax.bar(labels, values, color=['#1f77b4', '#1f77b4', '#d62728', '#2ca02c'])
ax.set_title("Efficiency Gains Waterfall Chart")
for i, value in enumerate(cumulative_values):
    ax.text(i, value, str(round(values[i], 2)), ha='center', va='bottom')

st.pyplot(fig)

# Summary Box
st.subheader("Summary")
st.write(f"**Baseline Cost**: €{baseline_cost:,}\n**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,}\n**Final Cost**: €{final_cost:,}")
