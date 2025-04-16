import streamlit as st
import pandas as pd
import pymysql

# ---------------------- DB Connection using PyMySQL ----------------------
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

# ---------------------- Sidebar ----------------------
st.set_page_config(page_title="University Dashboard", layout="wide")
st.sidebar.title("🎓 University Dashboard")

page = st.sidebar.radio("Navigate", ["🏠 Home", "🗓️ Timetable", "📁 Views"])

# ---------------------- Home Page ----------------------
if page == "🏠 Home":
    st.title("🏠 Home")
    st.success("Welcome, Master 👑")
    st.write("Use the sidebar to view the timetable or access database tables.")
#    st.image("https://i.imgur.com/JxbhRZj.png", width=600)  # Optional banner

# ---------------------- Timetable Page ----------------------
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

# ---------------------- Views Page ----------------------
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
        df = fetch_data("SELECT * FROM courseinfo")
        st.subheader("📚 Course Info")
        st.dataframe(df)

    elif view_option == "🧪 Exams":
        df = fetch_data("SELECT * FROM examschedule")
        st.subheader("🧪 Exam Schedule")
        st.dataframe(df)
