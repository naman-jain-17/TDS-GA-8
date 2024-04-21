import streamlit as st

st.title('Calculate largest among 3 numbers')

st.header('_Enter your inputs here:_ ')

num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')
num3 = st.number_input('Enter third number')

def maximum():
  lis = [num1 , num2 , num3]
  a = max(lis)
  st.success(f"Maximum = {a}")

if st.button("Calculate result"):
    maximum()
