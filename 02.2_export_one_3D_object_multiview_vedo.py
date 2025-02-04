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

# Load Object
mesh = load_object("Dataset/ModelNet10/chair/train/chair_0001.off")
plotter = Plotter(offscreen=True)  # Criar uma única instância para evitar abrir múltiplas janelas

for idx, (x, y, z) in enumerate(angles):
    # Rotate Object
    faces, vertices = rotation(mesh, x, y, z)

    new_mesh = Mesh([vertices, faces]).c("gray")

    # Limpa a cena antes de adicionar um novo objeto
    plotter.clear()
    plotter.add(mesh)

    # Renderiza e salva a imagem
    plotter.show(new_mesh, axes=0, size=(224, 224), interactive=False, resetcam=True)
    screenshot(f"output_{idx}.jpg")