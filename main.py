import streamlit as st

st.set_page_config(page_title="MediScribe", page_icon="📄")

st.markdown("""
    <style>
    .main {
        background-color: #07013d;
    }
    .sidebar .sidebar-content {
        background-color: #112b82;
        color: white;
    }
    .reportview-container .markdown-text-container {
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #112b82;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0d1d6d;
        color: #f0f2f6;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Welcome to MediScribe")
st.write("Navigate to different pages using the sidebar.")

st.image("C:/Users/jlena/hackmhs-24/MediScribe/img_doctor_patient.jpg", use_column_width=True)

st.header("About MediScribe")
st.write("""
MediScribe helps you to record, transcribe, and summarize your doctor visits effortlessly. 
With a user-friendly interface and advanced functionalities, you can easily manage and review your medical visits.
""")

st.header("How to Use MediScribe")
st.write("""
1. **Record Your Visit**: Navigate to the "Record Visit" page to start recording your visit.
2. **View Visits**: Go to the "View Visits" page to see all your past recordings and summaries.
3. **Summarization**: Our AI will transcribe and summarize your visit for easy review.
""")
