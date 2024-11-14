const canvas = document.getElementById("3d-model-canvas");
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  50,
  canvas.clientWidth / canvas.clientHeight,
  0.1,
  1000
);
camera.position.set(0, 1, 2.5);
camera.lookAt(0, 0.9, 0);

const renderer = new THREE.WebGLRenderer({
  canvas,
  alpha: true,
  antialias: true,
});
renderer.setSize(canvas.clientWidth, canvas.clientHeight);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setClearColor(0x000000, 0);

const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(3, 2, 10).normalize();
scene.add(directionalLight);

let mixer;

// Load FBX model
const loader = new THREE.FBXLoader();
loader.load(
  "./obj/Swing_Dancing.fbx",
  function (fbx) {
    fbx.scale.set(0.01, 0.01, 0.01);
    scene.add(fbx);

    mixer = new THREE.AnimationMixer(fbx);
    if (fbx.animations.length > 0) {
      const action = mixer.clipAction(fbx.animations[0]);
      action.play();
    }

    function animate() {
      requestAnimationFrame(animate);

      // Update mixer for animation
      if (mixer) {
        mixer.update(0.02);
      }

      updateCamera();
      renderer.render(scene, camera);
    }

    animate();
  },
  undefined,
  function (error) {
    console.error("An error happened", error);
  }
);

// Variables for target camera movement
let targetX = 0;
let targetY = 0;

// Mouse move event listener
document.addEventListener("mousemove", (event) => {
  const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
  const mouseY = (event.clientY / window.innerHeight) * 2 - 1;

  targetX = mouseX * 2; // Adjust multiplier for stronger effect if needed
  targetY = mouseY * 2;
});

// Update camera based on target values
function updateCamera() {
  camera.position.x += (-targetX - camera.position.x) * 1;
  camera.position.y += (targetY - camera.position.y) * 0.1;

  camera.lookAt(0, 0.9, 0);
}

// Handle resize
window.addEventListener("resize", () => {
  camera.aspect = canvas.clientWidth / canvas.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
});
