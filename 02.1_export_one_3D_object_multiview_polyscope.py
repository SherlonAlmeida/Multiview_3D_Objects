from shared_functions import *

# Multiview Angles
angles = [
    (121.72, 90.00, 148.28),
    (58.28, 90.00, 31.72),
    (121.72, 90.00, 148.28),
    (90.00, 31.72, 121.72),
    (90.00, 148.28, 58.28),
    (90.00, 148.28, 58.28),
    (31.72, 121.72, 90.00),
    (148.28, 58.28, 90.00),
    (31.72, 121.72, 90.00),
    (58.28, 90.00, 148.28),
    (121.72, 90.00, 31.72),
    (121.72, 90.00, 31.72)
]

# It is possible to use some angles combinations
#angles, n_angles = combine_rotations_3D(angle = 180)

# Initialize POLYSCOPE once
ps.set_program_name("3D Viewer")
ps.set_ground_plane_mode("none")
ps.set_window_size(224, 224)
ps.init()

# Load Object
mesh = load_object("Dataset/ModelNet10/chair/train/chair_0001.off")

# First rotation to register the mesh
faces, vertices = rotation(mesh, *angles[0])
ps_mesh = ps.register_surface_mesh("mesh", vertices, faces, color=(0.5, 0.5, 0.5), material="clay")

# Ensure proper visualization settings
ps.set_autocenter_structures(True)
ps.set_autoscale_structures(True)
ps.set_view_projection_mode("perspective")

for idx, (x, y, z) in enumerate(angles):
    # Rotate Object
    faces, vertices = rotation(mesh, x, y, z)

    # Update vertices of the existing mesh instead of re-registering
    ps_mesh.update_vertex_positions(vertices)

    # Capture screenshot
    ps.set_screenshot_extension(".jpg")
    ps.screenshot(filename=f"output_{idx}.jpg", transparent_bg=True)