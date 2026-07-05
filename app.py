import streamlit as st

# Title
st.title("Square and Cube Calculator")

# User input
number = st.number_input("Enter a number:", value=0.0)

# Calculate
square = number ** 2
cube = number ** 3

# Display results
st.subheader("Results")
st.write(f"**Square:** {square}")
st.write(f"**Cube:** {cube}")