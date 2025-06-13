# Import necessary packages
import streamlit as st
# import os

def show_lacrosse_prediction_dashboard():
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
  #  try:
   #    image_path = os.path.join(current_dir, "..", "images", "lacrosse_screenshot.png")
    #    if os.path.exists(image_path):
     #       st.image(image_path, caption="Lacrosse Project Screenshot", use_column_width=True)
      #     st.warning(f"Image not found at {image_path}. Please check the path.")
    # except Exception as e:
    #    st.error(f"Error loading image: {e}")

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
        This project was a fantastic learning experience, encompassing many aspects of the data science process.
        Some key takeaways include:

        * ** Takeaways and lessons here
        """
    )

    st.markdown("---")

    st.subheader("Project Resources:")
    st.write("[Link to Lacrosse Project GitHub Repository](Link to repo here)") 
    st.write("[Link to Live Demo (Link to streamlit site here)]") 
