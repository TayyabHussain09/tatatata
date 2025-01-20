import streamlit as st
from auth import add_user, login_user
from media import save_media, get_user_media, get_media_file
from database import create_tables

# Initialize database
create_tables()

# Authentication state
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None

def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if add_user(username, password):
            st.success("User created! Please log in.")
        else:
            st.error("Username already exists.")

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state["user_id"] = user[0]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials.")

def upload_media():
    st.subheader("Upload Media")
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "mp4", "mp3", "pdf"])
    if uploaded_file and st.button("Upload"):
        save_media(st.session_state["user_id"], uploaded_file.name, uploaded_file.read())
        st.success("File uploaded successfully!")

def view_media():
    st.subheader("Your Media Files")
    files = get_user_media(st.session_state["user_id"])
    for file_id, filename, upload_date in files:
        st.write(f"**{filename}** (Uploaded on {upload_date})")
        if st.button("Download", key=file_id):
            file = get_media_file(file_id)
            st.download_button(label="Download", data=file[1], file_name=file[0])

# Main app
if st.session_state["user_id"] is None:
    st.sidebar.title("Authentication")
    option = st.sidebar.radio("Choose an option", ["Login", "Sign Up"])
    if option == "Sign Up":
        signup()
    else:
        login()
else:
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose an option", ["Upload Media", "View Media"])
    if option == "Upload Media":
        upload_media()
    else:
        view_media()
