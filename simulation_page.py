import plotly.express as px # For plotting
import streamlit as st # For streamlit functions

# Import the two classes we need (g and Trial)
# from the des_classes.py file in the same folder
from des_classes import g, Trial
# Notice that we don't need to import simpy in here
# That's done in the des_classes script

if 'num_nurses_slider' not in st.session_state:
    st.session_state["num_nurses_slider"] = 5

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.logo("hsma_logo.png")

# Add a title to the top of the page
st.title("Clinic Simulation")

st.write(f"You set the number of nurses to {st.session_state['num_nurses_slider']}")

# Set up user inputs
with st.sidebar:
    mean_consult_time_slider = st.slider(
        "Choose the average consultation length",
        min_value=5, max_value=60, value=35
        )

    num_runs_numeric_input = st.number_input(
        "Set the number of runs", value=5
        )

# Overwrite the relevant attributes of the g class
# Make sure you match the attribute names from the g class
# that we define in the des_classes.py file!
g.number_of_nurses = st.session_state["num_nurses_slider"]
g.mean_n_consult_time = mean_consult_time_slider
g.number_of_runs = num_runs_numeric_input

# Define a run button
button_run_pressed = st.button("Run Simulation")

# Only run the following code if the run button is pressed
if button_run_pressed:
    # Make a spinner appear while the app calculations are running
    with st.spinner():

        # Run the simulation for the number of runs we've defined and save
        # the outputs into mean_results_df and detailed_run_results_df
        # (two pandas dataframes at varying levels of detail)
        mean_results_df, detailed_run_results_df = Trial().run_trial()

        # Display various outputs using those dataframes
        st.write("The median wait to see a nurse across all runs was " +
                f"{mean_results_df['Mean Q Time Nurse'].median():.1f} minutes")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(mean_results_df)

        with col2:

            st.subheader("Variation Across Runs in Mean Queue Time for Nurse")

            fig1 = px.box(mean_results_df,
                    x="Mean Q Time Nurse",
                    points="all",
                    range_x=[0, max(mean_results_df["Mean Q Time Nurse"])*1.1],
                    title="Mean Queueing Time for Nurse Per Run"
                    )

            st.plotly_chart(fig1)
