import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

# Function to get the current page name
def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]

# Function to create a sidebar with login/logout logic
def make_sidebar():
    with st.sidebar:
        st.title("💎 Diamond Corp")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/page1.py", label="Secret Company Stuff", icon="🔒")
            st.page_link("pages/page2.py", label="More Secret Stuff", icon="🕵️")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "streamlit_app":
            # Redirect to login page if not logged in
            st.switch_page("streamlit_app.py")

# Function to log out the user
def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")

# Main Cube function that can be imported and used in another file
def Cube():
    make_sidebar()
    st.title("Welcome to Diamond Corp")

    st.write("Please log in to continue.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in", type="primary"):
        if username == "your_valid_username" and password == "your_valid_password":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
        else:
            st.error("Incorrect username or password")
