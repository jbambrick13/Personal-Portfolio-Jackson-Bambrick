import streamlit as st
import os

def show_lacrosse_project():
    st.title("Lacrosse Championship Prediction & Visualization")

    st.write(
        """
        Describe project here
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

    st.header("Visualizations & Insights")
    # Placeholder for project screenshot
    try:
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "..", "images", "lacrosse_screenshot.png")
        if os.path.exists(image_path):
            st.image(image_path, caption="Lacrosse Project Screenshot", use_column_width=True)
        else:
            st.warning(f"Image not found at {image_path}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.write(
        """
        Beyond just predictions, a significant part of this project involved creating interactive visualizations
        using Plotly and Streamlit. These visualizations allow users to:

        * ** Description of dashboard here
        """
    )

    st.markdown("---")

    st.header("Journey and Lessons Learned")
    st.write(
        """
        This project was a fantastic learning experience, encompassing the full data science lifecycle.
        Some key takeaways include:

        * ** Takeaways and lessons here
        """
    )

    st.markdown("---")

    st.subheader("Project Resources:")
    st.write("[Link to Lacrosse Project GitHub Repository](Link to repo here)") 
    st.write("[Link to Live Demo (if applicable)]") 
