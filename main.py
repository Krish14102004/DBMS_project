import streamlit as st
import pandas as pd
import pymysql

# ----------------- Dummy Credentials -----------------
users = {
    "admin": "admin123",
    "faculty": "teacher456",
    "kr7819": "shailesh.05"
}

# ----------------- DB Connection -----------------
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="universitymanagementsystem",
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_data(query):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    conn.close()
    return pd.DataFrame(rows)

# ----------------- Login Logic -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login to University Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success("Login successful! Welcome, Master 👑")
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials! Try again.")
    st.stop()

# ----------------- After Login: Main App -----------------
st.set_page_config(page_title="University Dashboard", layout="wide")
st.sidebar.title("🎓 University Dashboard")

page = st.sidebar.radio("Navigate", ["🏠 Home", "🗓️ Timetable", "📁 Views"])

# ----------- Home Page -----------
if page == "🏠 Home":
    st.title("🏫 SRM University of Science & Technology")
    st.subheader("Learn. Leap. Lead.")
    st.markdown("### 📍 *Chennai, India*  &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 🏗️ *Established 2002*")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1: st.metric("🎓 Students", "52,000+ Full-Time")
    with col2: st.metric("🏛️ Departments", "19 Departments / 7 Schools")
    with col3: st.metric("👨‍🏫 Faculty", "3550+ Members")

    st.markdown("---")
    st.markdown("### 📚 Academic Programs Offered:")
    st.markdown("""
    - Bachelor of Business Administration  
    - BCA  
    - Information Technology  
    - Computer Science and Engineering  
    - Artificial Intelligence  
    - Diploma  
    - Electronics and Communication Engineering  
    - Law  
    - Master of Engineering  
    """)

    st.markdown("---")
    infra_cols = st.columns(4)
    infra_cols[0].success("🏠 Hostel Available")
    infra_cols[1].info("📚 Central Library")
    infra_cols[2].warning("🔬 Research Labs")
    infra_cols[3].error("📏 250 Acres Campus")

    st.markdown("---")
    st.markdown("#### 👨‍💼 Dean/Principal: *Dr. Rajiv Janardhanan*")
    st.markdown("Visit the official website: [SRM University](https://www.srmist.edu.in/)")
    st.image("https://www.srmist.edu.in/sites/default/files/2021-04/SRM_Logo_0.png", width=200)

# ----------- Timetable -----------
elif page == "🗓️ Timetable":
    st.title("🗓️ Faculty Timetable")
    st.info("Below is the weekly timetable for Prof. Arun Sharma")

    timetable_data = {
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        '9:00 - 10:00 AM': ['DBMS', 'DAA', 'DBMS', 'DAA', 'IoT'],
        '10:00 - 11:00 AM': ['-', 'DAA', '-', 'DAA', '-'],
        '11:00 - 12:00 PM': ['-', '-', '-', '-', '-'],
    }
    df = pd.DataFrame(timetable_data)
    st.dataframe(df, use_container_width=True)

# ----------- Views Section -----------
elif page == "📁 Views":
    st.title("📁 Database Views")
    view_option = st.selectbox("Choose View", [
        "🧑‍🎓 Students", "👨‍🏫 Faculty", "🏢 Hostels", "📚 Courses", "🧪 Exams"
    ])

    if view_option == "🧑‍🎓 Students":
        df = fetch_data("SELECT * FROM studentinfo")
        st.subheader("🧑‍🎓 Student Info")
        st.dataframe(df)

    elif view_option == "👨‍🏫 Faculty":
        df = fetch_data("SELECT * FROM facultyinfo")
        st.subheader("👨‍🏫 Faculty Info")
        st.dataframe(df)

    elif view_option == "🏢 Hostels":
        df = fetch_data("SELECT * FROM hosteloccupancy")
        st.subheader("🏢 Hostel Info")
        st.dataframe(df)

    elif view_option == "📚 Courses":
        df = fetch_data("SELECT * FROM coursesubjects")
        st.subheader("📚 Course Info")
        st.dataframe(df)

    elif view_option == "🧪 Exams":
        df = fetch_data("SELECT * FROM examschedule")
        st.subheader("🧪 Exam Schedule")
        st.dataframe(df)
