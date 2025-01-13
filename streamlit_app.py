import streamlit as st
from time import sleep
#from navigation import make_sidebar

#make_sidebar()


st.title("Ready to explore data with Cube!")

st.write("Please log in to continue.")

# Ask the user for their username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# In a real scenario, you'd validate these credentials with a database or some authentication mechanism.
# Here we are using placeholder checks just for demonstration.

if st.button("Log in", type="primary"):
    # Placeholder for checking valid username and password
    if username == "your_valid_username" and password == "your_valid_password":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/page1.py")
    else:
        st.error("Incorrect username or password")
