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

# Bar Chart for Visualization
labels = ['Orders Reduced', 'Direct Cost Savings (€)']
values = [orders_reduced, direct_cost_savings]

fig, ax1 = plt.subplots()

# First y-axis
ax1.bar(labels, values, color=['#1f77b4', '#2ca02c'])
ax1.set_xlabel('Metrics')
ax1.set_ylabel('Value')
ax1.set_title('Platform Efficiency Gains')

# Second y-axis for percentages
ax2 = ax1.twinx()
percentages = [orders_reduced/annual_orders*100, direct_cost_savings/(annual_cost_per_rep * sales_reps)*100]
ax2.set_ylabel('Percentage (%)')
ax2.plot(labels, percentages, color='r', marker='o')

# Adding text labels inside the bars
for i, (value, percentage) in enumerate(zip(values, percentages)):
    ax1.text(i, value, f"{value:,}\n({percentage:.1f}%)", ha='center', va='bottom')

st.pyplot(fig)

# Summary Box
st.subheader("Summary")
st.write(f"**Total Orders Reduced**: {orders_reduced:,}\n**Total Direct Cost Savings**: €{direct_cost_savings:,}")
