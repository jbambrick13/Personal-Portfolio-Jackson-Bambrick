import streamlit as st

def show_resume():
    st.title("My Resume")

    st.markdown("---")

    # --- Contact Information (Optional, or integrate into About Me) ---
    st.subheader("Contact Information")
    st.write("Email: your.email@example.com")
    st.write("LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
    st.write("GitHub: [Your GitHub Profile](https://github.com/yourprofile)")

    st.markdown("---")

    # --- Education Section ---
    st.header("Education")
    with st.expander("Expand Education"):
        # University 1
        st.subheader("University of Your Choice")
        st.write("**Degree:** Bachelor of Science in Data Science")
        st.write("**Graduation:** May 20XX")
        with st.expander("Courses & Achievements"):
            st.write("""
            * Relevant Coursework: Data Structures, Algorithms, Machine Learning, Statistical Modeling, Database Management.
            * Dean's List: [If applicable]
            * GPA: [If applicable]
            """)
        st.markdown("---") # Separator for multiple education entries

        # University 2 (if applicable)
        # st.subheader("Another University")
        # st.write("**Degree:** Master of Data Analytics")
        # st.write("**Graduation:** May 20XX")
        # with st.expander("Courses & Achievements"):
        #     st.write("""
        #     * Advanced topics in data science.
        #     """)

    st.markdown("---")

    # --- Experience Section ---
    st.header("Experience")
    with st.expander("Expand Experience"):
        # Job 1
        st.subheader("Data Analyst - Company Name")
        st.write("June 20XX – Present")
        with st.expander("Responsibilities & Achievements"):
            st.markdown("""
            * Analyzed large datasets to identify trends and provide actionable insights, leading to a 15% improvement in...
            * Developed and maintained SQL queries for data extraction and transformation.
            * Collaborated with cross-functional teams to define data requirements and reporting needs.
            * Created interactive dashboards using Tableau/Power BI to visualize key performance indicators.
            """)
        st.markdown("---")

        # Job 2 (if applicable)
        st.subheader("Intern Data Scientist - Another Company")
        st.write("May 20XX – August 20XX")
        with st.expander("Responsibilities & Achievements"):
            st.markdown("""
            * Assisted in building machine learning models for [specific task].
            * Preprocessed and cleaned raw data, improving data quality by X%.
            * Presented findings to stakeholders, contributing to...
            """)
        st.markdown("---")

    st.markdown("---")

    # --- Skills Section ---
    st.header("Skills")
    with st.expander("Expand Skills"):
        st.subheader("Programming Languages:")
        st.write("Python (Pandas, NumPy, Scikit-learn, Streamlit), SQL, R")

        st.subheader("Data Analysis & Visualization:")
        st.write("Data Cleaning, Exploratory Data Analysis, Matplotlib, Seaborn, Plotly, Tableau, Power BI")

        st.subheader("Machine Learning:")
        st.write("Regression, Classification, Clustering, Time Series Analysis")

        st.subheader("Databases:")
        st.write("MySQL, PostgreSQL, MongoDB")

        st.subheader("Tools & Platforms:")
        st.write("Git, GitHub, Docker, AWS (S3, EC2 - basic understanding)")

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

    # --- Awards & Certifications (Optional) ---
    # st.header("Awards & Certifications")
    # with st.expander("Expand Awards & Certifications"):
    #     st.write("Certification Name - Issuing Body (Year)")
    #     st.write("Award Name - Organization (Year)")
