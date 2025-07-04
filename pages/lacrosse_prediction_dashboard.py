# Import necessary packages
import streamlit as st

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
        This project provided me with great practice working on a vast range of data visualization and analysis;
        from cleaning data all the way through to visualizing results from probabliity based simulations! A more detailed
        look at my methodology is available below.
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
    with st.expander("Detailed Methodology Here"):
        st.write(
            """
            * **Data Collection:** The project began when I was granted access to 2 datasets by the gracious people at 
            LacorsseRefrence, again big thank you to Zack! One dataset was a CSV that contained a list of all 247 men's 
            lacrosse teams, each associated with a unique TeamID. The second CSV contained game data on every game from 
            February 19th through May 1st. There wre 50 features present for each game; however the ones relevant to the
            project were the game's ID and date, as well as each team's ID and ELO rating.
            * **Data Cleaning:** Cleaning the data was pretty straightforward: read in the seperate CSVs, remove the 
            extra features from the larger dataset, and then associate each team's ID with their teamname from the 
            other dataset. Essentially creating one managable dataframe that contained all the data needed to move forward.
            * **Tournament Modeling and Simulation Setup:** This phase of the project began with hard-coding in the seeding and tournament 
            logic for the 5 largest conference championships (ex: 1 seed has first round bye, 2 plays 5 and 4 plays 3).
            * **Monte Carlo Simulation Logic:** The winner of each game was decided using a Monte Carlo simulation
            and an ELO-based winning probability. Using each team's ELO going into the game, a precise likelihood on one 
            team winning was calculated. Then using a random number generator, the outcomes of dozens of game were predicted.
            The winning team's ELOs were updated (defeating a time with a higher ELO provides a bigger boost) and the following
            rounds of the tournaments were simulated using the same methods.
            * **Results and Visualiaztion:** After each tournament was simulated 1000 times, the results from every simulation 
            were saved to seperate CSVs, one for each conference tournament. These results were then loaded into a new dataframe
            using OS commands the name of each CSV. Then using Streamlit, I created and deployed an interactive dashboard that
            utilized charts created using Plotly. The dashboard allows viewers to view the winning probability distrubtuion for 
            the teams in each conference tournament.
            """
        )

    st.markdown("---")

    st.header("Skills Practiced")
    st.write(
        """
        This project was a fantastic learning experience, encompassing many aspects of the data science process.
        Some key takeaways include:

        * **Version Control:** Using GitHub for version control helped me keep track of changes
        * **Data Cleaning:** The initial dataset required significant cleaning and preprocessing to be usable.
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
