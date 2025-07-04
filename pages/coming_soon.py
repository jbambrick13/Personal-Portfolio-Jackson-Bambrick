# Import necessary packages
import streamlit as st

def show_coming_soon():
    st.title("Coming Soon: SQL Project")

    st.write(
        """
        This project is currently in development and will focus on advanced SQL techniques, database design, and data manipulation. 
        It will involve using an API to collect publicly available satellite data and using SQL to allow for complex queries, while 
        also taking advantadge of Tableu's visualization capacilites to tell data stories
        """
    )

    st.subheader("Anticipated Technologies:")
    st.write(
        """
        SQL, Tableau, Github, and possibly more to come!
        """
    )

    st.info("Stay tuned for updates! I'll be sharing progress and details on this page as the project develops.")
