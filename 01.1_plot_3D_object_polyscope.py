from shared_functions import *

# Parameters POLYSCOPE
ps.set_program_name("3D Viewer") #Set Program Name
ps.set_ground_plane_mode("none") #Disable "Ground"
ps.set_view_projection_mode("orthographic")

# Initialize POLYSCOPE
ps.init()

# Load Object
mesh = load_object("Dataset/ModelNet10/chair/train/chair_0001.off")

# Rotate Object
faces, vertices = rotation(mesh, 0, 0, 0)

# Center Vertices at (0,0,0)
vertices = center(vertices)

# Plot 3D Object
# Creating the object
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces, color=(0.5,0.5,0.5), material="clay")

# Set window size
ps.set_window_size(1200, 800)

# Visualization with POLYSCOPE (It is possible using VEDO to visualize as follows: mesh.show())
ps.set_autocenter_structures(True)  # Automatically center the object
ps.set_autoscale_structures(True)   # Fit the object in view
ps.set_view_projection_mode("perspective")  # Better visualization

ps.show()