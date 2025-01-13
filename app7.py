import streamlit as st
from time import sleep

# Set up the page title
st.title("Ready to explore data with Cube!")

st.write("Please log in to continue.")

# Ask the user for their username and password with unique keys
username = st.text_input("Username", key="username_input")  # Add a unique key for username input
password = st.text_input("Password", type="password", key="password_input")  # Add a unique key for password input

# Add custom CSS for the rotating cube animation
st.markdown("""
    <style>
        /* Container for the login form */
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            position: relative;
        }

        /* Animation for the rotating cube */
        .cube-container {
            position: absolute;
            top: 50%;
            right: 20px;
            transform: translateY(-50%);
            animation: rotate-cube 5s infinite linear;
        }

        /* Creating the cube using a div */
        .cube {
            width: 50px;
            height: 50px;
            background-color: #FFD700;
            animation: spin 5s infinite linear;
            transform-style: preserve-3d;
            transform: rotateX(0deg) rotateY(0deg);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .cube:before, .cube:after {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #FFD700;
        }

        /* Cube rotation keyframes */
        @keyframes rotate-cube {
            0% {
                transform: rotateY(0deg) rotateX(0deg);
            }
            100% {
                transform: rotateY(360deg) rotateX(360deg);
            }
        }

        @keyframes spin {
            0% {
                transform: rotateY(0deg);
            }
            100% {
                transform: rotateY(360deg);
            }
        }
    </style>
""", unsafe_allow_html=True)

# Create the login form container
with st.container():
    # Login form goes here
    with st.empty():
        username = st.text_input("Username", key="username_input")
        password = st.text_input("Password", type="password", key="password_input")

    if st.button("Log in", type="primary"):
        if username == "your_valid_username" and password == "your_valid_password":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
        else:
            st.error("Incorrect username or password")

# Cube container positioned on the right side with animation
st.markdown("""
    <div class="login-container">
        <div class="cube-container">
            <div class="cube"></div>
        </div>
    </div>
""", unsafe_allow_html=True)
