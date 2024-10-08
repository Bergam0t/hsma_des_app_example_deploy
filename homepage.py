import streamlit as st

if 'num_nurses_slider' not in st.session_state:
    st.session_state["num_nurses_slider"] = 5

st.logo("hsma_logo.png")

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title("Welcome to the simulation app")

st.write("Here's loads of information about what we're doing")

st.session_state["num_nurses_slider"] = st.slider(
    "Please enter the number of nurses", 1, 10, 5
    )
