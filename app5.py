import streamlit as st
import streamlit.components.v1 as components

# Set up the page configuration and title
st.set_page_config(page_title="Login Page", page_icon="🔲")

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

# Add Title
st.title("Login to Cube")

# Split the page into two sections using a container
st.markdown("""
    <div class="container">
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
    <title>Interactive Cube</title>
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
        
        // Create cube geometry
        var geometry = new THREE.BoxGeometry(1, 1, 1);
        var materials = [
            new THREE.MeshBasicMaterial({ color: 0xFF6347 }), // Front face (Policy)
            new THREE.MeshBasicMaterial({ color: 0x4682B4 }), // Back face (Economic)
            new THREE.MeshBasicMaterial({ color: 0x32CD32 }), // Top face (Dynamic)
            new THREE.MeshBasicMaterial({ color: 0xFFD700 }), // Bottom face
            new THREE.MeshBasicMaterial({ color: 0x8A2BE2 }), // Left face
            new THREE.MeshBasicMaterial({ color: 0xFF1493 })  // Right face
        ];
        var cube = new THREE.Mesh(geometry, materials);
        scene.add(cube);

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

