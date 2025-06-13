# Import necessary packages
import streamlit as st
# import os

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
        It showcases skills in data cleaning, feature engineering, probability based simulations, and interactive dashboard development.
        """
    )

    # Placeholder for project screenshot
   # try:
    #    current_dir = os.path.dirname(__file__)
    #   image_path = os.path.join(current_dir, "..", "images", "lacrosse_screenshot.png")
    #    if os.path.exists(image_path):
    #        st.image(image_path, caption="Lacrosse Project Screenshot", use_column_width=True)
    #    else:
    #        st.warning(f"Image not found at {image_path}. Please check the path.")
    # except Exception as e:
    #    st.error(f"Error loading image: {e}")

    st.markdown(
        """
        * **Technologies Used:** Python (Pandas, Scikit-learn, Streamlit, Plotly), [mention any others like SQL, etc.]
        * **Key Learnings:**
        * **View Project Details:** For an in-depth look at this project, please visit the **Lacrosse Championship Prediction & Visualization** page from the navigation menu.
        * **GitHub Repository:** [Link to Lacrosse Project GitHub Repo]
        """
    )

    st.markdown("---")

    # --- Coming Soon: SQL Project Placeholder ---
    st.header("Coming Soon: SQL Project")
    st.write(
        """
        A new project focusing on advanced SQL queries, database design, and data manipulation.
        """
    )
    # Possibly add generic "Coming Soon" image here.
    # try:
    #     coming_soon_image_path = os.path.join(current_dir, "..", "images", "coming_soon.png")
    #     if os.path.exists(coming_soon_image_path):
    #         st.image(coming_soon_image_path, caption="Coming Soon!", use_column_width=True)
    # except Exception as e:
    #     st.error(f"Error loading image: {e}")

    st.markdown("---")
