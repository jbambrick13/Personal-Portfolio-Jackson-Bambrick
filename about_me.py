#Import necessary packages
import streamlit as st
import os

def show_about_me():
    st.title("About Me")

    st.write(
        """
        Paragraph about my background, passions, relevant experiences, etc.
        """
    )

    # Placeholder for pic of me. Remember to create images file to store all pics in
    try:
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "..", "images", "your_picture.jpg")
        if os.path.exists(image_path):
            st.image(image_path, caption="This is me!", width=300)
        else:
            st.warning(f"Image not found at {image_path}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")

    # Explanation of the rest of the site
    st.header("Explore My Portfolio")
    st.write(
        """
        This portfolio website is designed to showcase my projects, skills, and experiences.
        Here's a quick overview of what you'll find:

        * **Resume:** An interactive and collapsible version of my resume, detailing my education, work experience, and technical skills.
        * **Project Central:** A hub for all my data related projects, featuring descriptions and screenshots.
        * **Lacrosse Championship Prediction & Visualization:** A deep dive into one of my key projects, including the methodology, visualizations, and lessons learned.
        * **Coming Soon: SQL Project:** A sneak peek at an upcoming project that will demonstrate my SQL proficiency.

        Feel free to navigate through the different sections using the dropdown menu on the left sidebar.
        I hope you enjoy exploring my work!
        """
    )
