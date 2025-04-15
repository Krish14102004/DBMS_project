import streamlit as st
import pymysql
import pandas as pd

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="universitymanagementsystem",
        cursorclass=pymysql.cursors.DictCursor
    )

# Reusable fetcher
def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return pd.DataFrame(rows)

# Sidebar menu
st.sidebar.title("📊 University Dashboard")
option = st.sidebar.selectbox("Select View", [
    "🏠 Home",
    "🧑‍🎓 Students",
    "👨‍🏫 Faculty",
    "🏢 Hostels",
    "📚 Courses",
    "🧪 Exams"
])

st.title("🎓 University Management Dashboard")

if option == "🏠 Home":
    st.subheader("Welcome, Master 👑")
    st.write("Use the sidebar to navigate through various views of your MySQL database.")

elif option == "🧑‍🎓 Students":
    st.subheader("Student Info")
    df = fetch_data("SELECT * FROM studentinfo")
    st.dataframe(df)

elif option == "👨‍🏫 Faculty":
    st.subheader("Faculty Info")
    df = fetch_data("SELECT * FROM facultyinfo")
    st.dataframe(df)

elif option == "🏢 Hostels":
    st.subheader("Hostel Occupancy")
    df = fetch_data("SELECT * FROM hosteloccupancy")
    st.dataframe(df)

elif option == "📚 Courses":
    st.subheader("Courses")
    df = fetch_data("SELECT * FROM coursesubjects")  # Use your view/table name
    st.dataframe(df)

elif option == "🧪 Exams":
    st.subheader("Exam Schedule")
    df = fetch_data("SELECT * FROM examschedule")  # Use your view/table name
    st.dataframe(df)
