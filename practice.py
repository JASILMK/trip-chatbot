import streamlit as st

st.title("Hello from upcode")

name = st.text_input("Enter your name:")
if st.button("click"):
    st.write(f"Hello {name},Welcome to upcode")