import streamlit as st
import streamlit.components.v1 as components
from time import sleep

# Set up the page configuration
st.set_page_config(page_title="Login Page with Cube", page_icon="🔲")

# Add custom CSS for layout and design
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            width: 100%;
        }

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

        .cube-container {
            width: 50%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .cube-wrapper {
            width: 80%;
            height: 80%;
            background-color: #e1f2f2;
            border-radius: 15px;
            padding: 20px;
        }

        .cube-wrapper canvas {
            width: 100%;
            height: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Function to display the login form and check credentials
def display_login_form():
    # Ask the user for their username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Placeholder for checking valid username and password
    if st.button("Log in"):
        if username == "your_valid_username" and password == "your_valid_password":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            sleep(0.5)
            st.experimental_rerun()  # Refresh the page to show the cube after login
        else:
            st.error("Incorrect username or password")

# Display the login form if the user is not logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    # Display login form
    st.title("Ready to explore data with Cube!")
    st.write("Please log in to continue.")
    display_login_form()
else:
    # If logged in, show the cube and additional content
    st.markdown("""
        <div class="container">
            <div class="login-form">
                <h2>Welcome to Cube!</h2>
                <p>Exploring data has never been easier. Let's start.</p>
            </div>

            <div class="cube-container">
                <div class="cube-wrapper">
                    <canvas id="cubeCanvas"></canvas>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Embed custom HTML, CSS, and JavaScript (for Cube animation)
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>3D Rotating Cube</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            body { margin: 0; overflow: hidden; }
            canvas { display: block; }
        </style>
    </head>
    <body>
        <script>
            // Set up the scene
            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            var renderer = new THREE.WebGLRenderer({canvas: document.getElementById('cubeCanvas')});
            renderer.setSize(window.innerWidth, window.innerHeight);
            
            // Create cube geometry with black color and green edges
            var geometry = new THREE.BoxGeometry(1, 1, 1);
            var materials = [
                new THREE.MeshBasicMaterial({ color: 0x000000 }), // Front face (black)
                new THREE.MeshBasicMaterial({ color: 0x000000 }), // Back face (black)
                new THREE.MeshBasicMaterial({ color: 0x000000 }), // Top face (black)
                new THREE.MeshBasicMaterial({ color: 0x000000 }), // Bottom face (black)
                new THREE.MeshBasicMaterial({ color: 0x000000 }), // Left face (black)
                new THREE.MeshBasicMaterial({ color: 0x000000 })  // Right face (black)
            ];

            var cube = new THREE.Mesh(geometry, materials);
            scene.add(cube);

            // Add green edges to the cube
            var edges = new THREE.EdgesGeometry(geometry);
            var line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: 0x00FF00 }));
            cube.add(line);

            // Position the camera
            camera.position.z = 3;

            // Animation loop for rotating the cube
            function animate() {
                requestAnimationFrame(animate);
                cube.rotation.x += 0.02;
                cube.rotation.y += 0.02;
                renderer.render(scene, camera);
            }

            animate();
        </script>
    </body>
    </html>
    """

    # Embed the HTML/JavaScript in Streamlit
    components.html(html_code, height=600, width=800)
