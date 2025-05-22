from shared_functions import *
from parameters import *
import os

path_dataset_3D = "./Dataset/ModelNet40/"
classes = os.listdir(path_dataset_3D)
print(classes)

# Create the Multiview folder (root)
path_dataset_multiview = "./ModelNet40-Multiview/"
if not os.path.exists(path_dataset_multiview):
    os.mkdir(path_dataset_multiview)

# Create a folder for each class
for curr_class in classes:
    curr_folder = path_dataset_multiview+curr_class+"/"
    if not os.path.exists(curr_folder):
        os.mkdir(curr_folder)
        os.mkdir(curr_folder+"train/")
        os.mkdir(curr_folder+"test/")

# Export Multiview Images
total_objs = 0
for curr_class in classes:
    fold = path_dataset_3D+curr_class+"/" #["train", "test"]
    for curr_fold in os.listdir(fold):
        objs = os.listdir(fold+curr_fold+"/")
        for curr_3D_obj in objs:
            total_objs += 1
            print(f"Creating Multiview ({total_objs}): {curr_3D_obj}")

            # Load Object
            path_curr_obj = fold+curr_fold+"/"+curr_3D_obj
            check_off_file(path_curr_obj) # Verifica se o Header do .OFF está OK, senão CORRIGE!
            mesh = load_object(path_curr_obj)
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
                output_filename = curr_3D_obj[:-4] + f"_{idx}.jpg"
                output_folder_path = f"{path_dataset_multiview}{curr_class}/{curr_fold}/"
                screenshot(output_folder_path+output_filename)
                print(f"({total_objs}) {output_folder_path+output_filename}")
            
            # # Stop if necessary (Debug Only)
            # if total_objs >= 1:
            #     exit(-1)