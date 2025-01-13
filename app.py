import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# Set up the page configuration and title
st.set_page_config(page_title="Welcome to Cube!", page_icon="🔲")

# Add custom CSS for navigation bar
st.markdown("""
    <style>
    .navbar {
        background-color: #223D3F;
        padding: 10px;
        color: white;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar with buttons
st.markdown('<div class="navbar"><a href="#">MoF</a><a href="#">Cash Flow</a><a href="#">LTFP</a></div>', unsafe_allow_html=True)

# Title text in the center
st.title("Welcome to Cube!")

# Create the 3D Cube using Plotly
cube_visible = st.checkbox("Show Cube", value=True)

if cube_visible:
    # Plot the 3D Cube
    fig = go.Figure(data=[go.Mesh3d(
        x=[1, -1, -1, 1, 1, -1, -1, 1],
        y=[1, 1, -1, -1, 1, 1, -1, -1],
        z=[1, 1, 1, 1, -1, -1, -1, -1],
        color='blue',
        opacity=0.5,
        flatshading=True
    )])

    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=4, range=[-1.5, 1.5]),
            yaxis=dict(nticks=4, range=[-1.5, 1.5]),
            zaxis=dict(nticks=4, range=[-1.5, 1.5]),
        ),
        title="3D Cube"
    )
    
    st.plotly_chart(fig)

# Display Bar Charts below the Cube

# Dummy data for the Fiscal Space bar chart
fiscal_space_data = pd.DataFrame({
    "Category": ["Oil Revenue", "Non-Oil Revenue", "Other Revenue"],
    "Amount": [1000, 500, 300]
})

# Dummy data for the Funding Demand bar chart
funding_demand_data = pd.DataFrame({
    "Category": ["BAU", "Strategies", "Giga Projects"],
    "Amount": [1200, 900, 600]
})

# Plot the Fiscal Space Bar Chart
fig_fiscal_space = px.bar(fiscal_space_data, x='Category', y='Amount', title="Fiscal Space")
st.plotly_chart(fig_fiscal_space)

# Plot the Funding Demand Bar Chart
fig_funding_demand = px.bar(funding_demand_data, x='Category', y='Amount', title="Funding Demand")
st.plotly_chart(fig_funding_demand)
