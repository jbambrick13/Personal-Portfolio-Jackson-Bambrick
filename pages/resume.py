# Import necessary package
import streamlit as st
def show_resume():
    st.title("My Resume")

    st.markdown("---")

    # --- Contact Information (Optional, or integrate into About Me) ---
    st.subheader("Contact Information")
    st.write("Email:jacksonbambrick253@gmail.com")
    st.write("LinkedIn: (Link here)")
    st.write("GitHub: (Link here)")

    st.markdown("---")

    # --- Education Section ---
    st.header("Education")
    with st.expander("Expand Education"):
        # University 1
        st.header("Gettybsurg College")
        st.write("**Degree:** Bachelor of Science in Physics with a Minor in Data Science")
        st.write("**Graduation:** May 2026")
        st.subheader("Courses & Achievements")
        st.write("""
        * Relevant Coursework: Data Structures, Algorithms, Machine Learning, Statistical Modeling, Database Management.
        * Dean's List: [Semesters here]
        * GPA: [Here]
        """)
    st.markdown("---")

    # --- Experience Section ---
    st.header("Experience")
    with st.expander("Expand Experience"):
        # Job 1
        st.header("Data Analyst Intern - Under Canvas")
        st.write("June 2026 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Responsibilities here
        """)
        st.markdown("---")

        # Job 2
        st.header("Intern Data Scientist - Empyrean Athletics")
        st.write("June 2026 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        *  Responsibilities here
        """)
        st.markdown("---")

    st.markdown("---")

    # --- Skills Section ---
    st.header("Skills")
    with st.expander("Expand Skills"):
        st.subheader("Programming Languages:")
        st.write("Python (Pandas, NumPy, Scikit-learn, Streamlit), SQL, R")

        st.subheader("Data Analysis & Visualization:")
        st.write("Data Cleaning, Exploratory Data Analysis, Matplotlib, Seaborn, Plotly, Tableau")

        st.subheader("Machine Learning:")
        st.write("Regression, Classification, Clustering")

       #st.subheader("Databases:")
       #st.write("MySQL, PostgreSQL, MongoDB")

       #st.subheader("Tools & Platforms:")
       #st.write("Git, GitHub, Docker, AWS (S3, EC2 - basic understanding)")

    st.markdown("---")

    # --- Projects Section (Briefly mention, link to Project Central) ---
    st.header("Projects")
    with st.expander("Expand Projects Summary"):
        st.write(
            """
            For a detailed look at my projects, please visit the **Project Central** page.
            Highlights include:
            * **Lacrosse Championship Prediction & Visualization:** A comprehensive project demonstrating predictive modeling and interactive data visualization.
            * **[Brief mention of another project]:** [A short description].
            """
        )

    st.markdown("---")

    # --- Awards & Certifications  ---
    # st.header("Awards & Certifications")
    # with st.expander("Expand Awards & Certifications"):
    #     st.write("Certification Name - Issuing Body (Year)")
    #     st.write("Award Name - Organization (Year)")