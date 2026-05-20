# Import needed packages
import streamlit as st

def show_DLA_sim_and_viz():
    st.title("Simulating and Visualizing Diffusion Limited Aggregation (DLA) in Python")

    # General description
    st.write(
        """
        This project was a fantastic opportunity to explore the fascinating world of Diffusion Limited Aggregation (DLA) 
        through both simulation and visualization, as a part of my class 'Computational Physics'.
        
        DLA is a stochastic process in which particles undergoing Brownian motion move randomly until they aggregate 
        and form complex fractal structures. This fundamental model helps explain how microscopic random processes 
        can create intricate macroscopic patterns — seen in real-world phenomena such as frost formation, 
        electrolytic deposition, and more.
        
        The goal of this project was to implement a computationally efficient DLA simulation in Python using 
        Monte Carlo methods, and to create compelling visualizations to illustrate the resulting growth patterns.
        """
    )

    # Links to resources
    st.subheader("Project Resources:")
    st.write("Link to GitHub Repository: https://github.com/jbambrick13/DLA-sim-viz")  
    st.markdown("---")

    # Project Overview & Methodology
    st.header("Project Overview & Methodology")
    st.write(
        """
        The simulation was built using a **Monte Carlo approach**, chosen for several key reasons:
        * DLA is a **stochastic process** — particle motion is random and cannot be described by simple formulas.
        * Simulating emergent patterns requires **thousands of particles and millions of steps**, demanding a scalable approach.
        * A **random walk** logic effectively models the Brownian motion that drives DLA behavior.
        
        Two core models were implemented:
        * **Inward Growth Model:** Particles are released from the boundary and walk inward until they aggregate 
        with an existing cluster.
        * **Outward Growth Model:** A single seed particle is anchored at the center of the grid, and the cluster 
        grows outward over time. This model is more complex but produces more realistic DLA fractal patterns 
        and allows for additional constraints to reduce simulation runtime.
        
        The simulation was developed in Python within a Jupyter Notebook environment (VSCode), 
        with interactive GIF visualizations rendered using the IPython library.
        
        A more detailed methodology is available in the expandable section below.
        """
    )

    # Detailed Methodology
    with st.expander("Detailed Methodology Here"):
        st.write(
            """
            * **Inward Growth Model:** Particles are spawned at the outer boundary of the grid and perform a 
            random walk until they make contact with the growing cluster, at which point they are anchored in place.
            
            * **Outward Growth Model:** Begins with a single seed particle at the center of the grid. 
            New particles are introduced and walk randomly until aggregating with the cluster. 
            This model incorporates additional boundary and proximity constraints to improve 
            computational efficiency while maintaining accuracy.
            
            * **Monte Carlo Simulation:** Randomness is introduced at each step of the particle's walk, 
            faithfully replicating the stochastic nature of Brownian motion that drives real-world DLA processes.
            
            * **Visualization:** Simulation states are captured and rendered as playable GIFs within 
            the Jupyter Notebook using the IPython HTML class, allowing for dynamic observation of 
            cluster growth over time.
            """
        )

    st.markdown("---")

    # Skills Section
    st.header("Technologies and Skills Applied")
    st.write(
        """
        This project provided deep exposure to scientific computing and simulation techniques. 
        Key technologies and skills include:
        * **Simulation:** Monte Carlo Methods, Random Walk Algorithms
        * **Scientific Computing:** Python (NumPy, Matplotlib)
        * **Visualization:** IPython (GIF rendering), Matplotlib
        * **Development Environment:** Jupyter Notebook, VSCode
        * **Mathematical Concepts:** Stochastic Processes, Brownian Motion, Fractal Geometry
        * **Version Control:** Git & GitHub
        """
    )
