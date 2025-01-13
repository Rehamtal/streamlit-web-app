import streamlit as st
import streamlit.components.v1 as components

# Set up the page configuration and title
st.set_page_config(page_title="Landing Page", page_icon="🔲")

# Add custom CSS for the navigation bar (smaller and hover effect)
st.markdown("""
    <style>
    body {
        margin: 0;
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f4;
    }
    .navbar {
        background-color: #223D3F;
        padding: 12px;
        color: white;
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .navbar a {
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        display: inline-block;
        transition: 0.3s;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
        border-bottom: 3px solid white;  /* White line under the button */
    }
    .navbar a:active {
        border-bottom: 3px solid white;
    }
    .container {
        text-align: center;
        padding-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar with buttons (MoF, Cash Flow, ELTP)
st.markdown('<div class="navbar"><a href="#mof">MoF</a><a href="#cashflow">Cash Flow</a><a href="#eltp">ELTP</a></div>', unsafe_allow_html=True)

# Title text in the center
st.title("Welcome to the Interactive 3D Cube!")

# Embed custom HTML, CSS, and JavaScript (for Three.js 3D Cube with interactivity)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive 3D Cube</title>
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
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Create cube geometry
        var geometry = new THREE.BoxGeometry();
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
        camera.position.z = 5;

        // Raycasting for clickable cube faces
        var raycaster = new THREE.Raycaster();
        var mouse = new THREE.Vector2();

        window.addEventListener('click', function(event) {
            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

            raycaster.update();
            var intersects = raycaster.intersectObject(cube);

            if (intersects.length > 0) {
                var clickedFace = intersects[0].face;
                let faceIndex = clickedFace.materialIndex;

                // Redirect based on which face was clicked
                let faceLinks = [
                    'https://your-report-url.com/mof',  // Policy
                    'https://your-report-url.com/cashflow',  // Economic
                    'https://your-report-url.com/eltp',  // Dynamic
                    'https://your-report-url.com/mof',   // Bottom face (same as Policy)
                    'https://your-report-url.com/cashflow',  // Left face (same as Economic)
                    'https://your-report-url.com/eltp'   // Right face (same as Dynamic)
                ];
                window.location.href = faceLinks[faceIndex];
            }
        }, false);

        // Animation loop for rotating the cube
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }

        animate();
    </script>
</body>
</html>
"""

# Embed the HTML/JavaScript in Streamlit
components.html(html_code, height=600, width=800)

