# Import needed packages
import streamlit as st

# Import page functions 
from pages import about_me
from pages import resume
from pages import project_central
from pages import lacrosse_prediction_dashboard
from pages import weather_project
from pages import coming_soon

# Page Configuration 
st.set_page_config(
    page_title="Jackson Bambrick - Personal Portfolio",
    layout="wide",
)

# Page Selection 
st.sidebar.title("Select Page")
page_selection = st.sidebar.selectbox(
    "Go to",
    [
        "About Me",
        "Resume",
        "Project Central",
        "Lacrosse Championship Prediction & Visualization Project",
        "Automated Weather Data Pipeline and Dashboard"
    ]
)

# Display Selected Page
if page_selection == "About Me":
    about_me.show_about_me()
elif page_selection == "Resume":
    resume.show_resume()
elif page_selection == "Project Central":
    project_central.show_project_central()
elif page_selection == "Lacrosse Championship Prediction & Visualization Project":
    lacrosse_prediction_dashboard.show_lacrosse_prediction_dashboard()
elif page_selection == "Automated Weather Data Pipeline and Dashboard":
    weather_project.show_weather_project()
elif page_selection == "Coming Soon: ML and the NBA G.O.A.T. Project":
    coming_soon.show_coming_soon()

