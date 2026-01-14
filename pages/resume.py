# Import necessary package
import streamlit as st

def show_resume():
    st.title("My Resume")

    st.markdown("---")

    # Contact Information
    st.subheader("Contact Information")
    st.write("Email: jacksonbambrick253@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/jackson-bambrick-bb1466250")
    st.write("GitHub: https://github.com/jbambrick13")

    st.markdown("---")

    # Experience Section
    st.header("Experience")
    with st.expander("Expand Experience"):
        # Job 1
        st.header("Data Engineer - Empyrean Athletics")
        st.write("June 2025 – Present")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        - Architected and deployed an automated end-to-end data platform using Python, Google Cloud Functions, and Firestore, integrating custom ETL pipelines with a statistical scoring algorithm to transform raw API/survey data into predictive NIL financial valuations for 200+ student athletes.
        - Designed a robust data scraping engine using Python and Pandas that optimized Apify agent usage via batch processing and smart filtering for 1500+ data points, reducing manual data collection efforts by 95% while maintaining strict schema compatibility with existing business reporting tools.
        - Contributing to the training and deployment of a novel NIL chatbot by curating multi-source datasets and refining LLM performance, directly supporting product demonstrations that secured customer buy-in.
        """)

        # Job 2
        st.header("Data Analytics Intern - Under Canvas")
        st.write("May 2025 – August 2025")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        - Cleaned and aggregated complex datasets including payroll data for over 200 employees across 12 locations. 
        """)
        st.markdown("""
	    - Performed statistical analysis to develop data-backed job postings for 49 positions.
        """)
        st.markdown("""
	    - Presented informative visuals and strategic recommendations to HR and Hospitality leadership, providing actionable language for job postings designed to attract top talent.
        """)
        st.markdown("---")

        # Job 3
        st.header("Market Research Associate - Nike Xcelerate Lacrosse")
        st.write("October 2024 - January 2025")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        - Managed large-scale data acquisition and database integrity for Nike Xcelerate, sourcing and normalizing thousands of data points on regional programs to build a high-accuracy market intelligence database. 
        """)
        st.markdown("---")
        
        # Job 4
        st.header("Youth Lacrosse Master Official")
        st.write("February 2018 - August 2022")
        st.subheader("Responsibilities & Achievements")
        st.markdown("""
        - Oversaw the training and evaluation of more than 100 new officials.
        """)
        st.markdown("""
	    - Ensured the safety of players and fair enforcement of league regulations in high pressure environments, while settling disputes between coaches, parents, and other officials.
        """)
        st.markdown("---")

    st.markdown("---")

    # Skills Section
    st.header("Skills")
    with st.expander("Expand Skills"):
        st.subheader("Programming Languages")
        st.write("Python & SQL")
        
        st.subheader("Data Engineering & Cloud")
        st.write("Google Cloud Functions, Firestore, PostgreSQL, ETL Pipeline Design, API Integration, Web Scraping, Agent Deployment, Git/Github")
        
        st.subheader("Data Science & ML")
        st.write("Pandas, NumPy, Predictive Modeling, Regression (Linear & Logistic), Classification, Clustering")

        st.subheader("Visualization & BI:")
        st.write("Tableau (Desktop & Public), Streamlit, Plotly, Seaborn, Matplotlib")

        st.subheader("Quantitative Analysis & Skills:")
        st.write("Monte Carlo Simulations, Hypothesis Testing, A/B Testing, Descriptive & Inferential Statistics, Statistical Normalization, Experimental Design")

        st.subheader("Tools and Frameworks")
        st.write("McStas Simulations (3D Modeling & particle simulations), Streamlit(Deployment and storytelling), Excel(Data handling and storage)")

        st.subheader("Soft Skills")
        st.write("Datastorytelling, Algorithmic thinking, Documentation habits, Attention to detial, Problem solving, ")

    st.markdown("---")

     # Education Section
    st.header("Education")
    with st.expander("Expand Education"):
        st.header("Gettybsurg College")
        st.write("**Degree:** Bachelor of Science in Physics with a Minor in Data Science")
        st.write("**Graduation:** May 2026")
        st.subheader("Gettysburg Men's Lacrosse")
        st.write("Student-athlete demonstrating discipline, leadership, and teamwork while balancing a 20+ hour weekly commitment with a rigorous academic workload")
        st.subheader("Courses & Achievements")
        st.write("""
        * Relevant Coursework: Capstone Research (Complex 3D Particle Simulations) Linear Algebra, Differential Equations, Statistical and Numerical Methods, Data Structures, Experimental Design
        * Dean's List: Fall ’22, Spring ’23, Fall ‘24
        * GPA: 3.75
        """)
    st.markdown("---")

    # Projects Section (Briefly mention, direct to Project Central)
    st.header("Projects")
    with st.expander("Expand Projects Summary"):
        st.write(
            """
            For a detailed look at my projects, please visit the **Project Central** page.
            Highlights include:
            * **Lacrosse Championship Prediction & Visualization:** A comprehensive project demonstrating probability based modeling using Python and interactive data visualization using Streamlit.
            * **Automated Weather Data Pipeline and Dashboard:** A project showcasing automated data collection, ETL processes, and real-time data visualization using Python, PostgreSQL, and Tableau.
            """
        )

    st.markdown("---")

     # Awards Section
    st.header("Awards & Activities")
    with st.expander("Expand Awards & Certifications"):
        st.write("""
        * UC Davis SQL for Data Science Certificate, August 2025 (https://www.coursera.org/account/accomplishments/certificate/Q5H9HSWWFBVB)
        * Sigma Pi Sigma, Physics National Honor Society
        * Chi Alpha Sigma, National Athletic Honor Society
        * Employee of the Month, July 2022, Safeway Supermarket
        """)
