#Import necessary packages
import streamlit as st
import os

def show_about_me():
    st.title("About Me")

    st.write(
        """
        Hello! My name is Jackson Bambrick and I'm currently a student-athlete at Gettysburg College in my senior year, pursuing a Bachelor of Science in Physics with a Minor in Data Science. I have a strong passion for data science and its
        applications, especially in sports analytics. My journey in data science has been fueled by my love for solving challenging problems and my desire to make data-driven decisions. This portfolio website is an introduction to me as 
        a person, as well as a showcase of my abilities and projects in data science.
        """ 
        )
    st.header("More About Me Here!") 
    with st.expander("Jackson Bambrick???"):
        st.write(
            """
            I grew up in a small city, Edgewood, about an hour south of Seattle in Washington State. My younger brother Joey and I spent most of our days outside, playing sports, building forts, and taking advantage of the beautiful 
            parks and forests around us. I have always been a sports enthusiast, playing lacrosse, football, and basketball throughout my childhood. My parents were always supportive of my brother and I, encouraging us to pursue our
            passions and providing us with the opportunities to do so. They taught us to take pride in anything we do, to strive to achieve what we desired, and that working hard is easier when you enjoy what you do.

            During my high school years at Bellarmine Prep, a Jesuit school in Tacoma, I was fortunate to receive a valuable education that prioritized critical thinking, problem-solving, and ethical decision-making, while reinforcing 
            the foundational value of hard-work that my parents instilled in me. I was also able to continue playing lacrosse at a high-level, which taught me the importance of teamwork, discipline, and perseverance. While in hig school, 
            I developed a strong interest in the use of data to analyze sports and predict outcomes; I was fascinated by how stats were being used to find patterns that provided teams and players with advantages over their competition.
            Specifically within the game of basketball, teams were adding entire departments dedicated to analyzing player performance and finding trends within the game, leading to the "three-point revolution" that has transformed the 
            sport over the last few years.  
            
            After high school, I have been fortunate to continue my education at Gettysburg College, where I am currently pursuing a Bachelor of science degree in Physics with a minor in Data Science. My time at Gettysburg has been 
            amazing, allowing me to further develop my analytical skills and deepen my understanding of data science. I have been able to take courses in data structures, algorithms, machine learning, and statistical modeling, which have
            provided me with a solid foundation in the field. Additionally, I have been able to apply my knowledge in real-world projects, which are showcased in this portfolio. As a member of the men's lacrosse team, I have had the 
            opportunity to compete on a nationally ranked team, teaching me the importance of growing out of uncomfortable situations, overcoming challenges, effective time management, and learning from failures.
            """
        )

    # Picutre of me
    try:
        current_dir = os.path.dirname(__file__)
        # Ensure 'Images' matches the capital 'I' of your folder
        image_path = os.path.join(current_dir, "Images", "This_is_me.jpg") 
        if os.path.exists(image_path):
            st.image(image_path, caption="Jackson Bambrick", width=300)
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
        I hope you enjoy exploring my work, please reach out with any questions or curiosities !
        """
    )
