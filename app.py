import streamlit as st

# Title
st.title("Welcome to My Interactive Web Page! 🌟")

# Text input for user name
name = st.text_input("What's your name?", "")

if name:
    st.write(f"Hello, {name}! 👋")

# Slider for selecting age
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# Radio button for user choices
option = st.radio("Choose your favorite fruit:", ("Apple", "Banana", "Orange"))
st.write(f"Your favorite fruit is: {option}")

# Button for submitting
if st.button("Submit"):
    st.write("Thank you for submitting! 🎉")
