# Import needed packages
import streamlit as st

# Import page functions 
from pages import about_me
from pages import resume
from pages import project_central
from pages import lacrosse_prediction_dashboard
from pages import coming_soon

# --- Page Configuration ---
st.set_page_config(
    page_title="Jackson Bambrick - Personal Portfolio",
    layout="wide",
)

# --- Page Selection ---
st.sidebar.title("Select Page")
page_selection = st.sidebar.selectbox(
    "Go to",
    [
        "About Me",
        "Resume",
        "Project Central",
        "Lacrosse Championship Prediction & Visualization Project",
        "Coming Soon: SQL Project"
    ]
)

# --- Display Selected Page ---
if page_selection == "About Me":
    about_me.show_about_me()
elif page_selection == "Resume":
    resume.show_resume()
elif page_selection == "Project Central":
    project_central.show_project_central()
elif page_selection == "Lacrosse Championship Prediction & Visualization Project":
    lacrosse_prediction_dashboard.show_lacrosse_prediction_dashboard()
elif page_selection == "Coming Soon: SQL Project":
    coming_soon.show_coming_soon()