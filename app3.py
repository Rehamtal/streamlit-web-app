import streamlit as st
import streamlit.components.v1 as components

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

# Embed custom HTML and JavaScript (for Three.js 3D Cube with interactivity)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Cube Interaction</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; }
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
        var material = new THREE.MeshBasicMaterial({ color: 0x44aa88, wireframe: true });
        var cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Position the camera
        camera.position.z = 5;

        // Cube face interaction setup
        let faceColors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']; // Colors for the faces
        let faceLinks = [
            'https://your-report-url.com/mof',  // Policy
            'https://your-report-url.com/cashflow',  // Economic
            'https://your-report-url.com/eltp',  // Dynamic
            'https://your-report-url.com/mof',
            'https://your-report-url.com/cashflow',
            'https://your-report-url.com/eltp'
        ];

        // Adding interactivity on each cube face
        var raycaster = new THREE.Raycaster();
        var mouse = new THREE.Vector2();
        var intersects;

        window.addEventListener('click', function(event) {
            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

            raycaster.update();
            intersects = raycaster.intersectObject(cube);

            if (intersects.length > 0) {
                var clickedFace = intersects[0].face;
                let faceIndex = clickedFace.materialIndex;

                // Redirect based on which face was clicked
                window.location.href = faceLinks[faceIndex];
            }
        }, false);

        // Render loop to animate the cube
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

# Embed the HTML/JavaScript in the Streamlit app
components.html(html_code, height=600, width=800)

