# Import necessary packages
import streamlit as st

def show_project_central():
    st.title("Project Central")

    st.write(
        """
        Welcome to Project Central! Here you'll find a collection of my data science and analytics projects.
        """
    )

    st.markdown("---")

    # Project 1: Lacrosse Championship Prediction & Visualization
    st.header("Lacrosse Championship Prediction & Visualization")

    st.write(
        """
        This project involved building a predictive model to forecast the outcomes of lacrosse championship games
        and creating interactive visualizations to explore the data and model results.
        It is intended to showcase skills in data cleaning, feature engineering, probability based simulations, and 
        interactive dashboard development.
        """
    )

    st.markdown(
        """
        * **Technologies Used:** Python (Pandas, Numpy, and Scikit-learn), Visualitzation Tools (Streamlit and Plotly) and Github (Version Control)
        * **Skills and Concepts Applied:** Probabilistic Modeling and Simulation, Creating Interactive Visualization Dashboards,  Algorithmic Thinking, and Practical Data Handling.
        * **View Project Details:** For an in-depth look at this project, please visit the **Lacrosse Championship Prediction & Visualization** page from the navigation menu.
        * **GitHub Repository:** https://github.com/jbambrick13/NCAA-D3-Tournaments-Sim-Visualization
        """
    )

    st.markdown("---")

    # Project 2: Weather Project
    st.header("Automated Weather Data Pipeline and Dashboard")
    st.write(
        """
        This project is a full-stack data pipeline that automatically collected real-time weather data,
        built a historical dataset over time, and presents the findings in an interactive dashboard.
        A Python script fetches data from the OpenWeatherMap API, loads it into a PostgreSQL database, 
        and a Tableau dashboard connects directly to this data source for visualization. The project
        highlights skills in data engineering, ETL automation, database management, and business intelligence
        """
    )

    st.markdown(
        """
        * **Technologies Used:** Python (Pandas, Numpy, requests, and psycopg2), PostgreSQL(Data Storage and Management), Visualization Tools (Tableau Desktop and Tableau Public) and Github (Version Control)
        * **Skills and Concepts Applied:** Data Extraction, Transformation, and Loading (ETL), Time Series Analysis, and Data Visualization.
        * **View Project Details:** For an in-depth look at this project, please visit the **Weather Project** page from the navigation menu.
        * **GitHub Repository:** https://github.com/jbambrick13/Weather-Project/tree/main
        """
    )
