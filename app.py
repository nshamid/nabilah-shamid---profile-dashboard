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
    st.caption("Professional Certifications, Courses, and Recognitions")
    st.divider()

    tab1, tab2, tab3 = st.tabs([
        "🏅 Certification",
        "📚 Certificate Courses",
        "🏆 Achievements"
    ])

    # ==================================================
    # TAB 1 : CERTIFICATION (PROFESSIONAL)
    # ==================================================
    with tab1:
        st.subheader("Professional Certification")

        certifications = [
            {
                "title": "PCEP™ – Certified Entry-Level Python Programmer",
                "provider": "Python Institute",
                "issued": "December",
                "score": "96%",
                "credential": "PCEP-30-02",
                "logo": "python.png",
                "analysis": [
                    ("Python and Programming Fundamentals", "100%"),
                    ("Control Flow – Conditionals & Loops", "93%"),
                    ("Data Collections (Lists, Tuples, Dictionaries, Strings)", "100%"),
                    ("Functions and Exceptions", "93%")
                ],
                "link": "https://verify.openedg.org/?id=wHfH.pVSj.Boya"
            }
        ]

        for cert in certifications:
            with st.expander(f"🐍 {cert['title']}", expanded=False):
                col1, col2 = st.columns([1, 4])

                with col1:
                    st.image(
                        f"assets/logos/{cert['logo']}",
                        width=70
                    )

                with col2:
                    st.markdown(f"**Issued by:** {cert['provider']}")
                    st.markdown(f"**Issued:** {cert['issued']}")
                    st.markdown(f"**Score:** **{cert['score']}**")
                    st.markdown(f"**Credential ID:** {cert['credential']}")

                    st.markdown("### 📊 Section Analysis")
                    for section, score in cert["analysis"]:
                        st.write(f"- **{section}:** {score}")

                    st.markdown(
                        f"🔗 [View Certificate]({cert['link']})",
                        unsafe_allow_html=True
                    )

    # ==================================================
    # TAB 2 : CERTIFICATE COURSES
    # ==================================================
    with tab2:
        st.subheader("Technical Courses & Learning Programs")

        courses = [
            {
                "title": "Python Essentials 1",
                "provider": "Cisco Networking Academy",
                "issued": "December",
                "logo": "cisco.png",
                "link": "https://www.credly.com/badges/cd59cd56-c381-4dde-b05e-673ba88283ef/linked_in_profile"
            },
            {
                "title": "Data Classification and Summarization Using IBM Granite",
                "provider": "IBM",
                "issued": "August",
                "logo": "ibm.png",
                "link": "https://www.credly.com/badges/cda5b7fe-7f13-45fe-b020-02c65a19d603/linked_in_profile"
            },
            {
                "title": "Introduction to Microsoft Azure Cloud Services",
                "provider": "Microsoft",
                "issued": "February",
                "logo": "microsoft.png",
                "link": "https://www.coursera.org/account/accomplishments/verify/UZ7QXTZDP4W2"
            },
            {
                "title": "Generative AI with Large Language Models",
                "provider": "DeepLearning.AI",
                "issued": "January",
                "logo": "deeplearningai.png",
                "link": "https://www.coursera.org/account/accomplishments/verify/8TWZ43UN349R"
            },
            {
                "title": "Generative AI: Introduction and Applications",
                "provider": "IBM",
                "issued": "January",
                "logo": "ibm.png",
                "link": "https://www.coursera.org/account/accomplishments/verify/XST8F3VNHKTG"
            },
            {
                "title": "Introduction to Machine Learning on AWS",
                "provider": "Amazon Web Services (AWS)",
                "issued": "January",
                "logo": "aws.png",
                "link": "https://www.coursera.org/account/accomplishments/verify/9H0EE5828KNQ"
            },
            {
                "title": "Science and Technology Track: Cloud, ML & Security Academy",
                "provider": "US-ASEAN STIC Program",
                "issued": "January",
                "logo": "asean.png",
                "link" : "https://drive.google.com/file/d/1uC-jhoj2gf__KlOycjqJj6n953pzaM46/view?usp=sharing"
            },
            {
                "title": "Build and Deploy Machine Learning Solutions on Vertex AI",
                "provider": "Google Cloud",
                "issued": "-",
                "logo": "googlecloud.png",
                "link": "hhttps://www.cloudskillsboost.google/public_profiles/6637f7ad-6cb5-46db-8449-d3916cbe98dc/badges/9773107"
            },
            {
                "title": "Create ML Models with BigQuery ML",
                "provider": "Google Cloud",
                "issued": "-",
                "logo": "googlecloud.png",
                "link": "https://www.cloudskillsboost.google/public_profiles/6637f7ad-6cb5-46db-8449-d3916cbe98dc/badges/9834275"
            },
            {
                "title": "Explore Generative AI with the Vertex AI Gemini API",
                "provider": "Google Cloud",
                "issued": "-",
                "logo": "googlecloud.png",
                "link": "https://www.cloudskillsboost.google/public_profiles/6637f7ad-6cb5-46db-8449-d3916cbe98dc/badges/9837793"
            },
        ]

        for course in courses:
            with st.expander(f"📘 {course['title']}", expanded=False):
                col1, col2 = st.columns([1, 4])

                with col1:
                    st.image(
                        f"assets/logos/{course['logo']}",
                        width=60
                    )

                with col2:
                    st.markdown(f"**Provider:** {course['provider']}")
                    st.markdown(f"**Issued:** {course['issued']}")
                    st.markdown(
                        f"🔗 [View Certificate]({course['link']})",
                        unsafe_allow_html=True
                    )

    # ==================================================
    # TAB 3 : ACHIEVEMENTS
    # ==================================================
    with tab3:
        st.subheader("Achievements & Recognitions")

        achievements = [
            {
                "title": "3rd Place – Creative Business Challenge",
                "event": "Sinergi Festival",
                "date": "December",
                "description": "Awarded 3rd place in the Creative Business Challenge category.",
                "link": "https://drive.google.com/drive/folders/12CN2T8tWvljNOq8ptkZd_uKsoScneavJ?usp=sharing"
            },
            {
                "title": "Machine Learning Operations Portfolio Program Mentee",
                "event": "RISTEK Sister In Tech 2025",
                "date": "August",
                "description": "Selected as a mentee focusing on Machine Learning Operations and portfolio development.",
                "link": "https://verify.ristek.cs.ui.ac.id/"
            },
            {
                "title": "Data Science Project-Based Internship Program",
                "event": "ID/X Partners",
                "date": "July",
                "description": "Completed a project-based virtual internship as a Data Scientist.",
                "link": "https://drive.google.com/file/d/1CXlm9O8ghh3Rh6OFbngtmhfMGETDcaJL/view?usp=sharing"
            }
        ]

        for ach in achievements:
            with st.expander(f"🏆 {ach['title']}", expanded=False):
                st.markdown(f"**Event / Program:** {ach['event']}")
                st.markdown(f"**Date:** {ach['date']}")
                st.write(ach["description"])
                st.markdown(
                    f"🔗 [View Details]({ach['link']})",
                    unsafe_allow_html=True
                )


elif page == "Projects":
    st.title("🚀 Projects")
    st.info("This section will be added next.")
