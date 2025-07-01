# Import necessary packages
import streamlit as st
# import os

def show_lacrosse_prediction_dashboard():
    st.title("Lacrosse Championship Prediction & Visualization")

    st.write(
        """
        The goal of this project was to build a predictive model to forecast the outcomes of lacrosse championship games. 
        Specifically, using a Monte Carlo simulation approach, I aimed to predict the likelihood of each team advacning 
        through their tournament and winning the championship based on team's ELO rating going into their respective 
        tournaments. 

        The initial dataset was generously provided by the good people at Lacrosse Reference (https://lacrossereference.com/) 
        big thanks to them because without their data, this project would not have been possible.
        """
    )

    st.markdown("---")

    st.header("Project Overview & Methodology")
    st.write(
        """
        Overview and methodlogy here
        """
    )
    st.markdown("---")
    
    st.write(
        """
        Beyond just predictions, a significant part of this project involved creating interactive visualizations
        using Plotly and Streamlit. These visualizations allow users to explore the predictions and view the
        probability distributions of each team's chances of advancing through the tournament and winning their
        championship.
        """
    )

    st.markdown("---")

    st.header("Skills Practiced")
    st.write(
        """
        This project was a fantastic learning experience, encompassing many aspects of the data science process.
        Some key takeaways include:

        * ** Version Control:** Using GitHub for version control helped me keep track of changes
        * ** Data Cleaning:** The initial dataset required significant cleaning and preprocessing to be usable.
        * **Modeling:** Implementing the Monte Carlo simulation required a solid understanding of probability. 
        * **Visualization:** Creating interactive visualizations with Streamlit and Plotly allowed me to present data in an accessible way.
        * **Deployment:** Deploying the Streamlit app provided hands-on experience with web application development.
        * **Collaboration:** Working with the Lacrosse Reference dataset taught me the importance of colloboration and data sharing in the 
            data science community.
        """
    )

    st.markdown("---")

    st.subheader("Project Resources:")
    st.write("Link to Lacrosse Project GitHub Repository: https://github.com/jbambrick13/NCAA-D3-Tournaments-Sim-Visualization") 
    st.write("Link to Live Demo: https://jbambrick13-ncaa-d3-tour-tournament-prediction-dashboard-rxnd3f.streamlit.app/") 
