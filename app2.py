import streamlit as st
import plotly.graph_objects as go

# Set up the page configuration and title
st.set_page_config(page_title="Landing Page", page_icon="🔲")

# Add custom CSS for navigation bar (smaller with white line under)
st.markdown("""
    <style>
    .navbar {
        background-color: #000000;
        padding: 5px;
        color: white;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
    }
    .navbar a {
        color: white;
        padding: 10px 15px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
        border-bottom: 3px solid white;  /* White line under the button */
    }
    .navbar a:active {
        border-bottom: 3px solid white;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar with buttons (with white line hover effect)
st.markdown('<div class="navbar"><a href="#mof">MoF</a><a href="#cashflow">Cash Flow</a><a href="#eltp">ELTP</a></div>', unsafe_allow_html=True)

# Title text in the center
st.title("Welcome to the Landing Page!")

# Create the 3D Cube using Plotly (with clickable blocks)
st.subheader("Click on the blocks of the Cube to go to the respective report.")

# 3D Cube Creation
cube_visible = st.checkbox("Show 3D Cube", value=True)

if cube_visible:
    # Create a 3D cube using Plotly
    fig = go.Figure(data=[go.Mesh3d(
        x=[1, -1, -1, 1, 1, -1, -1, 1],
        y=[1, 1, -1, -1, 1, 1, -1, -1],
        z=[1, 1, 1, 1, -1, -1, -1, -1],
        color='blue',
        opacity=0.5,
        flatshading=True
    )])

    # Update layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=4, range=[-1.5, 1.5]),
            yaxis=dict(nticks=4, range=[-1.5, 1.5]),
            zaxis=dict(nticks=4, range=[-1.5, 1.5]),
        ),
        title="3D Cube - Click on the blocks"
    )
    
    st.plotly_chart(fig)

    # Add clickable buttons for each cube block below
    st.write("### Cube Blocks (Click below to go to report):")
    if st.button('Policy'):
        st.markdown('[Go to MoF Report](https://your-report-url.com)', unsafe_allow_html=True)  # Replace with the actual link for MoF report
    if st.button('Economic'):
        st.markdown('[Go to Cash Flow Report](https://your-report-url.com)', unsafe_allow_html=True)  # Replace with the actual link for Cash Flow report
    if st.button('Dynamic'):
        st.markdown('[Go to ELTP Report](https://your-report-url.com)', unsafe_allow_html=True)  # Replace with the actual link for ELTP report
