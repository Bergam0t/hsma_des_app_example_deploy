import streamlit as st

pg = st.navigation(
    [
        st.Page("homepage.py", title="Welcome!", icon=":material/add_circle:"),
        st.Page("simulation_page.py", title="Clinic Simulation")
    ]
)

pg.run()
