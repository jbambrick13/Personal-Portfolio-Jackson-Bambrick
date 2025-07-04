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

    # --- Project 1: Lacrosse Championship Prediction & Visualization ---
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

    # --- Coming Soon: SQL Project Placeholder ---
    st.header("Coming Soon: SQL Project")
    st.write(
        """
        A new project focusing on advanced SQL queries, database design, and data scraping.
        """
    )

    st.markdown("---")
