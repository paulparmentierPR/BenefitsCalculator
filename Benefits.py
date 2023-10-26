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
order_reduction_percent = (orders_reduced / annual_orders) * 100
cost_savings_percent = (direct_cost_savings / (annual_cost_per_rep * sales_reps)) * 100

# Summary Box
st.subheader("Summary")
st.write(f"**Total Orders Reduced**: {orders_reduced:,} ({order_reduction_percent:.2f}%)\n**Total Direct Cost Savings**: €{direct_cost_savings:,} ({cost_savings_percent:.2f}%)")

# Waterfall Charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Orders Waterfall Chart
ax1.set_ylim(0, annual_orders * 1.2)
labels1 = ['Baseline', 'Reduction', 'Remaining']
values1 = [annual_orders, -orders_reduced, annual_orders - orders_reduced]
ax1.bar(labels1, values1, color=['#1f77b4', '#2ca02c', '#1f77b4'], bottom=[0, annual_orders, 0])
ax1.set_title("Order Reduction")
ax1.text(0, annual_orders / 2, f'{annual_orders:,}', ha='center', va='center', fontsize=10)
ax1.text(1, annual_orders - (orders_reduced / 2), f'Reduction\n{orders_reduced:,}\n({order_reduction_percent:.2f}%)', ha='center', va='center', fontweight='bold', fontsize=10)
ax1.text(2, (annual_orders - orders_reduced) / 2, f'{annual_orders - orders_reduced:,}', ha='center', va='center', fontsize=10)

# Monetary Savings Waterfall Chart
ax2.set_ylim(0, annual_cost_per_rep * sales_reps * 1.2)
labels2 = ['Baseline', 'Reduction', 'Remaining']
values2 = [annual_cost_per_rep * sales_reps, -direct_cost_savings, (annual_cost_per_rep * sales_reps) - direct_cost_savings]
ax2.bar(labels2, values2, color=['#1f77b4', '#2ca02c', '#1f77b4'], bottom=[0, annual_cost_per_rep * sales_reps, 0])
ax2.set_title("Monetary Savings")
ax2.text(0, (annual_cost_per_rep * sales_reps) / 2, f'€{annual_cost_per_rep * sales_reps:,}', ha='center', va='center', fontsize=10)
ax2.text(1, (annual_cost_per_rep * sales_reps) - (direct_cost_savings / 2), f'Reduction\n€{direct_cost_savings:,}\n({cost_savings_percent:.2f}%)', ha='center', va='center', fontweight='bold', fontsize=10)
ax2.text(2, ((annual_cost_per_rep * sales_reps) - direct_cost_savings) / 2, f'€{(annual_cost_per_rep * sales_reps) - direct_cost_savings:,}', ha='center', va='center', fontsize=10)

st.pyplot(fig)
