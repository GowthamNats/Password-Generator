import streamlit as st
import math
import random

st.title("Welcome to the Password Generator")

letters_in = st.number_input("How many alphabets would you like?")
digits_in = st.number_input("How many numbers would you like?")
symbols_in = st.number_input("How many symbols would you like?")

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!"#$%&_*+,-.'

password_list = []

if st.button("Generate"):
    for letter in range(1, math.floor(letters_in) + 1):
        password_list.append(random.choice(letters))

    for digit in range(1, math.floor(digits_in) + 1):
        password_list.append(random.choice(digits))

    for digit in range(1, math.floor(symbols_in) + 1):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    st.header("Generated Password: ")
    st.write("".join(password_list))