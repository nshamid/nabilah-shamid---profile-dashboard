import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Portfolio Dashboard",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- SIDEBAR NAVIGATION ----------------
with st.sidebar:
    st.title("📁 Portfolio")
    st.caption("Interactive Portfolio Dashboard")

    st.divider()

    page = st.radio(
        "Navigation",
        ["About Me", "Certificates", "Projects"]
    )

    st.divider()


# ==================================================
# ================= ABOUT ME PAGE ==================
# ==================================================
if page == "About Me":

    st.title("👩‍💻 About Me")
    st.caption("Personal Background & Profile Overview")
    st.divider()

    # ---------- PROFILE SECTION (PHOTO + DESCRIPTION) ----------
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "assets/images/profile.jpeg",
            caption="Nabilah Shamid",
            use_container_width=True
        )

    with col2:
        st.subheader("Profile Summary")
        st.write(
            """
            I am an **Informatics Engineering Student** with a strong passion for technology,
            particularly in **Data Science, Machine Learning, and Artificial Intelligence**.
            I have experience in **public speaking** as a Master of Ceremony (MC) and possess
            strong **communication and public relations skills**.

            I am recognized for being **responsible, adaptable**, and capable of performing
            effectively in both **team-based and individual environments**. I am highly
            enthusiastic about continuous learning and self-improvement, supported by a
            solid foundation in **data science, machine learning, and AI fundamentals**.
            """
        )

        st.markdown("**🎯 Main Interests**")
        st.write(
            """
            - Data Science  
            - Machine Learning  
            - Artificial Intelligence  
            """
        )

    st.divider()

    # ---------------- TABS ----------------
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧾 Background",
        "🔗 Social Media",
        "🏢 Organization & Experience",
        "🛠️ What Can I Do"
    ])

    # ---------------- TAB 1 : BACKGROUND ----------------
    with tab1:
        st.subheader("Background Overview")
        st.write(
            """
            I am currently pursuing a degree in **Informatics Engineering**, focusing on
            developing both **technical expertise** and **soft skills** to prepare for a
            professional career in the technology industry.

            My academic journey and extracurricular involvement have shaped my interest
            in data-driven problem solving and intelligent systems.
            """
        )

    # ---------------- TAB 2 : SOCIAL MEDIA ----------------
    with tab2:
        st.subheader("Connect With Me")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 📸 Instagram")
            st.markdown("[Visit Instagram](https://www.instagram.com/nblhshamid_)")

        with col2:
            st.markdown("### 💼 LinkedIn")
            st.markdown("[Visit LinkedIn](https://www.linkedin.com/in/nabilahshamid)")

        with col3:
            st.markdown("### 💻 GitHub")
            st.markdown("[Visit GitHub](https://github.com/nshamid)")

    # ---------------- TAB 3 : ORGANIZATION & EXPERIENCE ----------------
    with tab3:
        st.subheader("Organization & Experience")

        st.markdown("### 🏛️ BEM KM Fasilkom UNSRI")
        st.write(
            """
            - **Head of Academic Division**, Research & Technology Department (2025)  
            - **Staff of External Relations Department** (2024)
            """
        )

        st.markdown("### 🎓 Bakti BCA Scholarship")
        st.write("- **Awardee of Bakti BCA Scholarship 2025**")

        st.markdown("### 📜 Training & Certification")
        st.write(
            """
            - **International Training & Certification**, Faculty of Computer Science  
              (Python Certified Entry-Level Programmer – PCEP)
            """
        )

        st.markdown("### 🚀 Programs & Internships")
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
        st.subheader("Capabilities & Skills")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧠 Technical Skills")
            st.write(
                """
                - Data Analysis & Data Preparation  
                - Machine Learning Model Development  
                - Artificial Intelligence Fundamentals  
                - Python Programming  
                - SQL & Data Management  
                - Dashboard & Data Visualization  
                """
            )

        with col2:
            st.markdown("### 🤝 Non-Technical Skills")
            st.write(
                """
                - Public Speaking (MC & Presentation)  
                - Communication & Public Relations  
                - Leadership & Team Collaboration  
                - Time Management & Responsibility  
                - Adaptability & Continuous Learning  
                """
            )

        st.markdown("### 🧰 Tools & Technologies")
        st.write(
            """
            - Python  
            - Streamlit  
            - Pandas, NumPy, Scikit-learn  
            - Git & GitHub  
            - Google Colab  
            """
        )

# ==================================================
# PLACEHOLDER PAGE (biar tidak error saat diklik)
# ==================================================
elif page == "Certificates":
    st.title("📜 Certificates & Achievements")
    st.info("This section will be added next.")

elif page == "Projects":
    st.title("🚀 Projects")
    st.info("This section will be added next.")
