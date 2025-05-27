from shared_functions import *

# Load Object
# mesh = load_object("GeneralFiles/Example-ModelNet/guitar_0001.off") # OFF
mesh = load_object("GeneralFiles/Example-ShapeNet/model_normalized.obj") # OBJ

# Rotate Object
faces, vertices = rotation(mesh, 0, 0, 0)

# Center Vertices at (0,0,0)
vertices = center(vertices)

# Plot 3D Object
mesh = Mesh([vertices, faces]).c("gray")
show(mesh, axes=0, size=(1200, 800), interactive=True)