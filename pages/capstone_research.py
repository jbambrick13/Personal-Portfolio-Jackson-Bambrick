# Import necessary packages
import streamlit as st
import os

# Define image paths
current_dir = os.path.dirname(__file__)
data_table = os.path.join(current_dir, "Images", "full_data_table.png") 

def show_capstone_research():
    st.title("Physics Capstone Research Project: Modeling the Search for the V₅ Potential")
    # General description
    st.write(
        """
        The fall semester of my senior year, I had the incredible opportunity to work on a capstone research project in physics 
        under the guidance of Professor Bret Crawford. The project focuses on optimizing an experimental setup being prepared for
        the Spallation Neutron Source at Oak Ridge National Laboratory to search for the elusive V₅ potential energy.
        
        On this site you can find an brief overview of the project, including the abstract
        and key takeaways from the experience. If you're interested in learning more feel 
        free to reach out to me directly!
        """ 
    )

    # Project Abstract
    st.subheader("Project Abstract:")
    st.write(
        """
        In the field of fundamental symmetries, there is an intensifying search for new, weakly coupled interactions beyond the 
        Standard Model. This paper focuses on the exotic V₅ potential, a parity-even, spin- and velocity-dependent interaction
        that acts as a pseudo-magnetic field and would cause Larmor precession in polarized slow neutron beams. I use McStas 
        neutron spin-transport simulations to model the next planned experimental setup in the search for interactions caused 
        by the V₅ potential by the Neutrons Spin Rotation collaboration. I report on the changes to the beam’s phase space and 
        count rate when changing the location of our apparatus further downstream on the BL13b cold neutron beamline at the
        Spallation Neutron Source at Oak Ridge National Laboratory.
        """
    )
    
    # 
    st.subheader("Key Results and Figures")
    st.write(
        """
        Below are some of the key figures and results from the simulations I conducted as 
        part of this project. 
        """
    )
    st.write(
        """
        * **Figure 1:** Total intensity of the neutron beam as a function of gap distance.
        """
    )
    try:
        intensity = os.path.join(current_dir, "Images", "AnTotal_Intensity_vs_GapDistance.png") 
        if os.path.exists(intensity):
            st.image(intensity, caption="Jackson Bambrick", width=300)
        else:
            st.warning(f"Image not found at {intensity}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")
    st.write(
        """
        * **Figure 2:** Percent loss in monitor counts versus gap distance.
        """
    )
    try:
        monitor_loss = os.path.join(current_dir, "Images", "Percent_Loss_Monitor_vs_GapDistance.png") 
        if os.path.exists(monitor_loss):
            st.image(monitor_loss, caption="Jackson Bambrick", width=300)
        else:
            st.warning(f"Image not found at {monitor_loss}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")
    st.write(
        """
        * **Figure 3:** Percent loss in total system counts versus gap distance.
        """
    )
    try:
        total_loss = os.path.join(current_dir, "Images", "Percent_Loss_TotalSystem_vs_GapDistance.png") 
        if os.path.exists(total_loss):
            st.image(total_loss, caption="Jackson Bambrick", width=300)
        else:
            st.warning(f"Image not found at {total_loss}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")
    st.write(
        """
        * **Table 1:** Summary of transmission rates for different gap distances.
        """
    )
    try:
        tr_table = os.path.join(current_dir, "Images", "tr_table.png") 
 
        if os.path.exists(tr_table):
            st.image(tr_table, caption="Jackson Bambrick", width=300)
        else:
            st.warning(f"Image not found at {tr_table}. Please check the path.")
    except Exception as e:
        st.error(f"Error loading image: {e}")


    st.markdown("---")
    # Thanks Section
    st.header("Gratitudes and Acknowledgements")
    st.write(
        """
        This research was an amazing opportunity that I am incredibly grateful for. I am glad to
        have had the chance to contribute to meaningful work in the field of physics, and I 
        want to thank the following people for their support and guidance throughout the project:

        * **Professor Bret Crawford** Chair of the Physics Department at Gettysburg College and my research advisor.
        * **Dipto Provast, G'25:** Prior student researcher whose foundational work greatly aided my project.
        * **The Neutron Spin Rotation Collaboration:** For their pioneering research and for providing the experimental framework that
            guided my simulations.
        """
    )

    st.markdown("---")

    
