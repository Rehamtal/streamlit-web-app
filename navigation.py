import streamlit as st

def display_login_form():
    # Add custom CSS for layout and design
    st.markdown("""
        <style>
            .login-form {
                width: 40%;
                padding: 40px;
                background-color: #ffffff;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
                border-radius: 10px;
                border: 1px solid #ddd;
            }

            .login-form h2 {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #223D3F;
            }

            .login-form label {
                font-size: 16px;
                margin-bottom: 10px;
                color: #333;
            }

            .login-form input {
                width: 100%;
                padding: 12px;
                margin-bottom: 20px;
                font-size: 16px;
                border-radius: 5px;
                border: 1px solid #ddd;
                box-sizing: border-box;
            }

            .login-form input[type="checkbox"] {
                width: auto;
                margin-right: 8px;
            }

            .login-form button {
                width: 100%;
                padding: 12px;
                font-size: 16px;
                background-color: #223D3F;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            .login-form button:hover {
                background-color: #1A2A2B;
            }
        </style>
    """, unsafe_allow_html=True)

    # Add Title
    st.title("Login to Cube")

    # Display login form
    st.markdown("""
        <div class="login-form">
            <h2>Ready to explore data with Cube!</h2>
            <form action="#">
                <label for="name">Enter your Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Enter your Email Address:</label>
                <input type="email" id="email" name="email" required>

                <label for="terms">
                    <input type="checkbox" id="terms" name="terms">
                    I agree to the Terms and Conditions
                </label>

                <button type="submit">Login</button>
            </form>
        </div>
    """, unsafe_allow_html=True)
