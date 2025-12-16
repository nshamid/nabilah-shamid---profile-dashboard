import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="👩‍💻",
    layout="wide"
)

st.title("About Me")
st.write("")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Background",
    "Social Media",
    "Organization & Experience",
    "What Can I Do"
])

# ---------------- TAB 1 : BACKGROUND ----------------
with tab1:
    st.subheader("Profile Summary")

    st.write(
        """
        I am an **Informatics Engineering Student** with a strong passion for technology,
        particularly in **Data Science, Machine Learning, and Artificial Intelligence**.
        I have experience in **public speaking** as a Master of Ceremony (MC) and possess
        strong **communication and public relations skills**.

        I am known for being **responsible, adaptable**, and able to perform effectively
        in both **team-based and individual work environments**. I am highly enthusiastic
        about continuous learning and self-development, with a solid foundation in
        **data analysis, machine learning, and AI concepts**.
        """
    )

    st.markdown("**Field of Interest:**")
    st.write("- Data Science")
    st.write("- Machine Learning")
    st.write("- Artificial Intelligence")

# ---------------- TAB 2 : SOCIAL MEDIA ----------------
with tab2:
    st.subheader("Connect With Me")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Instagram")
        st.markdown(
            "[Visit Instagram](https://www.instagram.com/yourusername)",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("### LinkedIn")
        st.markdown(
            "[Visit LinkedIn](https://www.linkedin.com/in/yourusername)",
            unsafe_allow_html=True
        )

# ---------------- TAB 3 : ORGANIZATION & EXPERIENCE ----------------
with tab3:
    st.subheader("Organization & Professional Experience")

    st.markdown("### BEM KM Fasilkom UNSRI")
    st.write(
        """
        - **Head of Academic Division**, Research & Technology Department (2025)
        - **Staff of External Relations Department** (2024)
        """
    )

    st.markdown("### Bakti BCA Scholarship Awardee")
    st.write("- **Awardee of Bakti BCA Scholarship 2025**")

    st.markdown("### Training & Certification")
    st.write(
        """
        - **International Training & Certification**, Faculty of Computer Science  
          (Python Certified Entry-Level Programmer – PCEP)
        """
    )

    st.markdown("### Professional Programs & Internships")
    st.write(
        """
        - **Frontend Engineer**, Braintopia  
        - **Machine Learning Operations Portfolio Program**, SISTECH  
        - **Project-Based Virtual Intern – Data Scientist**,  
          ID/X Partners x Rakamin Academy
        """
    )

# ---------------- TAB 4 : WHAT CAN I DO ----------------
with tab4:
    st.subheader("What Can I Do")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Technical Skills")
        st.write(
            """
            - Data Analysis & Data Preparation  
            - Machine Learning Model Development  
            - Basic Artificial Intelligence Concepts  
            - Python Programming  
            - SQL & Data Handling  
            - Dashboard & Data Visualization  
            """
        )

    with col2:
        st.markdown("### Non-Technical Skills")
        st.write(
            """
            - Public Speaking (MC & Presentation)  
            - Communication & Public Relations  
            - Team Collaboration & Leadership  
            - Time Management & Responsibility  
            - Adaptability & Continuous Learning  
            """
        )

    st.markdown("### Tools & Technologies")
    st.write(
        """
        - Python  
        - Streamlit  
        - Pandas, NumPy, Scikit-learn  
        - Git & GitHub  
        - Google Colab  
        """
    )
