import streamlit as st

def calculate(number):

    return number ** 2, number ** 3

st.title("Square and Cube Calculator")

number = st.number_input("Enter a number:", value=0.0)

square, cube = calculate(number)

st.subheader("Results")
st.write(f"**Square:** {square}")
st.write(f"**Cube:** {cube}")