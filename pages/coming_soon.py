# Import necessary packages
import streamlit as st

def show_coming_soon():
    st.title("Coming Soon: SQL Project")

    st.write(
        """
        This project is currently in development and will focus on advanced SQL techniques, database design, and data manipulation. 
        It will involve scraping publicly available satellite data and using SQL to allow for complex  queries. 
        """
    )

    st.subheader("Anticipated Technologies:")
    st.write(
        """
        SQL, Tableau, Github, add others throughout
        """
    )

    st.info("Stay tuned for updates! I'll be sharing progress and details on this page as the project develops.")
