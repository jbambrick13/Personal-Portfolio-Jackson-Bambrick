# Import necessary package
import streamlit as st
def show_resume():
    st.title("My Resume")

    st.markdown("---")

    # --- Contact Information (Optional, or integrate into About Me) ---
    st.subheader("Contact Information")
    st.write("Email:jacksonbambrick253@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/jackson-bambrick-bb1466250")
    st.write("GitHub: https://github.com/jbambrick13")

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
        * Dean's List: Fall ’22, Spring ’23, Fall ‘24
        * GPA: 3.72
        """)
    st.markdown("---")

    # --- Experience Section ---
    st.header("Experience")
    with st.expander("Expand Experience"):
        # Job 1
        st.header("Data Analyst Intern - Under Canvas")
        st.write("May 2025 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Engaging in a critical data analytics project focused on promoting pay equity within Under Canvas's hospitality operations. 
        * Responsibilities include analyzing complex compensation data from diverse hospitality roles to identify opportunities for equitable take-home pay.
        * Gaining hands-on experience in data manipulation, visualization, and presenting actionable insights directly to the full HR team
        """)
        st.markdown("---")

        # Job 2
        st.header("Market Research Associate - Nike Xcelerate Lacrosse")
        st.write("Fall/Winter 2024")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Conducted comprehensive online research to identify and document 114 local lacrosse programs and over 300 key contacts.
        * Handled accurate compiling and input of thousands of data points into corresponding database, ensuring dataset integrity and accuracy.
        * Met 100% of deadlines and productivity goals while maintaining high-quality standards.
        """)
        st.markdown("---")

        # Job 3
        st.header("Intern Data Scientist - Empyrean Athletics")
        st.write("June 2025 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Placeholder for responsibilities and achievements
        """)
        st.markdown("---")

    st.markdown("---")

    # Skills Section
    st.header("Skills")
    with st.expander("Expand Skills"):
        st.subheader("Programming Languages:")
        st.write("Python (Pandas, NumPy, Scikit-learn, Seaborn), SQL, R")
        
        st.subheader("Data Analysis and Statistics")
        st.write("Descriptive and Inferential Statistics, Experimental Design, Hypothesis Testing, A/B Testing")
        
        st.subheader("Modeling and Mathematics")
        st.write("Probability theory, Simulations, Numerical Methods, Optimization, Linear ALgebra")

        st.subheader("Visualization:")
        st.write("Seaborn, Plotly, Tableau")

        st.subheader("Machine Learning:")
        st.write("Regression, Classification, Clustering, Model Evaluation")

        st.subheader("Tools and Technologies")
        st.write("Git/Github (Version control and collaboration), Streamlit(Deployment and storytelling), Excel(Data handling and storage)")

        st.subheader("Soft Skills")
        st.write("Datastorytelling, Algorithmic thinking, Documentation habits, Attention to detial, Problem solving, ")

    st.markdown("---")

    # Projects Section (Briefly mention, direct to Project Central)
    st.header("Projects")
    with st.expander("Expand Projects Summary"):
        st.write(
            """
            For a detailed look at my projects, please visit the **Project Central** page.
            Highlights include:
            * **Lacrosse Championship Prediction & Visualization:** A comprehensive project demonstrating probability based modeling using Python and interactive data visualization using Streamlit.
            * **Coming Soon! Satellite Search:** A project focused on using SQL and Tableau to analyze satellite location data.
            """
        )

    st.markdown("---")

     # Awards Section
    st.header("Awards & Activities")
    with st.expander("Expand Awards & Certifications"):
        st.write("Employee of the Month, July 2022, Safeway Supermarket")
        st.write("Sigma Pi Sigma, Physics National Honor Society")
        st.write("Chi Alpha Sigma National Athletic Honor Society ")
