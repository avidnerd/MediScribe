import streamlit as st
import sqlite3

st.set_page_config(page_title="View Visits", page_icon="📅")

st.markdown("""
    <style>
    .main {
        background-color: #07013d;
    }
    </style>
    """, unsafe_allow_html=True)

conn = sqlite3.connect('visits.db')
c = conn.cursor()

st.title("All Recorded Visits")

if st.button('Show All Visits'):
    visits = c.execute('SELECT id, transcript, summary FROM visits').fetchall()
    for visit in visits:
        st.write(f"Visit ID: {visit[0]}")
        with st.expander("Transcript"):
            st.write(visit[1])
        with st.expander("Summary"):
            st.write(visit[2])

conn.close()
