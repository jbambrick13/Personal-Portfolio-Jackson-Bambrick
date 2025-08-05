# Import necessary packages
import streamlit as st

def show_weather_project():
    st.title("Automated Weather Data Pipeline and Dashboard")
    # General description
    st.write(
        """
    The goal of this project was to design and build a robust, automated system for collecting and analyzing real-time weather data, 
    demonstrating a comprehensive understanding of the entire data lifecycle from extraction to visualization.
        """
    )

    # Links to Dashboard and Repo
    st.subheader("Project Resources:")
    st.write("Link to Live Demo: https://public.tableau.com/app/profile/jackson.bambrick/viz/AutomatedUSCityWeatherAnalysis/Dashboard1") 
    st.write("Link to Weather Project GitHub Repository: https://github.com/jbambrick13/Weather-Project") 

    st.markdown("---")
    # Methodology Overview
    st.header("Project Overview & Methodology")
    st.write(
        """
        This was a fantastic experience working with the classic ETLV architecture:
        * Extract: A Python script, scheduled to run automatically, calls the OpenWeatherMap API to fetch current weather data for a 
        predefined list of cities.
        * Transform: The raw JSON data from the API is cleaned and structured in Python. Key transformations include combining separate 
        rain and snow fields into a single total_precipitation metric to standardize analysis
        * Load: The clean, transformed data is loaded into a weather_data table within a PostgreSQL database for persistent storage.
        * Visualize: A Tableau dashboard connects directly to the PostgreSQL database, providing an interactive and up-to-date visualization 
        of weather trends.
        A more detailed methodology is available in the expandable section below.
        """
    )
    # Detailed Methodology
    with st.expander("Detailed Methodology Here"):
        st.write(
            """
            * **Data Extraction:** An automated Python script leverages the requests library to call the OpenWeatherMap API, 
            fetching current weather conditions for multiple cities at regular intervals.
            * **Data Storage:** The script connects to a PostgreSQL database using the psycopg2 library and loads the 
            cleaned data into a structured table, building a unique historical dataset over time.
            * **Data Visualization:** An interactive Tableau dashboard is connected directly to the PostgreSQL database. 
            It features time-series charts, comparative bar charts, and KPI cards that allow users to dynamically filter
              and explore the data to uncover trends and insights.
            """
        )

    st.markdown("---")
    # Skills Section
    st.header("Technologies and Skills Applied")
    st.write(
        """
        This project was a fantastic learning experience, encompassing many aspects of the data science process.
        Some key takeaways include:

        * Data Extraction: Python (requests library), OpenWeatherMap API
        * Data Transformation: Python (datetime library)
        * Data Storage: PostgreSQL (SQL)
        * Time Series Analysis: Python (Pandas library)
        * Descriptive Statistics: Python (Numpy library)
        * Data Visualization: Tableau Desktop and Tableau Public
        * Automation: Time Scheduling Logic
        * Version Control: Git & GitHub
        """
    )