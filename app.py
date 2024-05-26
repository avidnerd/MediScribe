import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Record Visit", "View Visits"])

# Navigation logic
if page == "Home":
    st.write("## Welcome to MediScribe")
    st.write("Navigate to different pages using the sidebar.")
elif page == "Record Visit":
    exec(open("record.py").read())
elif page == "View Visits":
    exec(open("visits.py").read())
