# Import necessary package
import streamlit as st

def show_resume():
    st.title("My Resume")

    st.markdown("---")

    # Contact Information
    st.subheader("Contact Information")
    st.write("Email:jacksonbambrick253@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/jackson-bambrick-bb1466250")
    st.write("GitHub: https://github.com/jbambrick13")

    st.markdown("---")

    # Education Section
    st.header("Education")
    with st.expander("Expand Education"):
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

    # Experience Section
    st.header("Experience")
    with st.expander("Expand Experience"):
        # Job 1
        st.header("Data Analyst Intern - Under Canvas")
        st.write("May 2025 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Engaging in a critical data analytics project focused on promoting pay equity within Under Canvas's hospitality operations. 
        * Analyzing payroll data for 61 employees across 7 locations in order to identify discrepencies between base wages and true earning potentials.
        * Gaining hands-on experience in data manipulation, visualization, and presenting actionable insights directly to the full HR team.
        """)
        st.markdown("---")

        # Job 2
        st.header("Intern Data Scientist - Empyrean Athletics")
        st.write("June 2025 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Developing a novel model to provide NIL valuations to over 200 high-school basketball players.
        * Structuring and overseeing the entire lifecycle of the NIL valuation model, leading the process from initial 
        algorithm design and data collection strategies to overseeing the deployment of the model to the Empyrean App.
        * Automted data collection from diverse sources by developing web scrapers to gather sports statistics data 
        and utilizing API techniques to gather social media data.
        """)
        st.markdown("---")

        # Job 3
        st.header("Market Research Associate - Nike Xcelerate Lacrosse")
        st.write("Fall/Winter 2024")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        * Conducted comprehensive online research to collect data on 114 local lacrosse programs and over 300 key contacts.
        * Handled accurate compiling and input of thousands of data points, ensuring dataset integrity and accuracy.
        * Met 100% of deadlines and productivity goals while maintaining high-quality standards.
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
        st.write("Probability Theory, Simulations, Numerical Methods, Optimization, Linear ALgebra")

        st.subheader("Visualization:")
        st.write("Seaborn, Plotly, Tableau")

        st.subheader("Machine Learning:")
        st.write("Regression, Classification, Clustering, Model Evaluation")

        st.subheader("Data Collection:")
        st.write("Web Scraping, API Usage, Comprehensive Research Methods")

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
