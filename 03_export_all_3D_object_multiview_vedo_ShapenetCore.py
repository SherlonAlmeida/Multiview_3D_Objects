from shared_functions import *
from parameters import *
import os

path_dataset_3D = "./Dataset/ShapeNetCore_v2/"
#classes = os.listdir(path_dataset_3D)
#print(classes)
# all_classes = ['02691156', '02747177', '02773838', '02801938', '02808440', '02818832', '02828884', '02843684', '02871439', '02876657', '02880940', '02924116', '02933112', '02942699', '02946921', '02954340', '02958343', '02992529', '03001627', '03046257', '03085013', '03207941', '03211117', '03261776', '03325088', '03337140', '03467517', '03513137', '03593526', '03624134', '03636649', '03642806', '03691459', '03710193', '03759954', '03761084', '03790512', '03797390', '03928116', '03938244', '03948459', '03991062', '04004475', '04074963', '04090263', '04099429', '04225987', '04256520', '04330267', '04379243', '04401088', '04460130', '04468005', '04530566', '04554684']
# ainda_falta_rodar = ['02747177', '02773838', '02801938', '02808440', '02818832', '02828884', '02843684', '02871439', '02876657', '02880940', '02924116', '02933112', '02942699', '02946921', '02954340', '02958343', '02992529', '03001627', '03046257', '03085013', '03207941', '03211117', '03261776', '03325088', '03337140', '03467517', '03513137', '03593526', '03624134', '03636649', '03642806', '03691459', '03710193', '03759954', '03761084', '03790512', '03797390', '03928116', '03938244', '03948459', '03991062', '04004475', '04074963', '04090263', '04099429', '04225987', '04256520', '04330267', '04379243', '04401088', '04460130', '04468005', '04530566', '04554684']
classes = ['02691156']

# Create the Multiview folder (root)
path_dataset_multiview = "./ShapeNetCore-Multiview/"
if not os.path.exists(path_dataset_multiview):
    os.mkdir(path_dataset_multiview)

# Create a folder for each class
for curr_class in classes:
    curr_folder = path_dataset_multiview+curr_class+"/"
    if not os.path.exists(curr_folder):
        os.mkdir(curr_folder)

# Export Multiview Images
total_objs = 0
for curr_class in classes: # Current Class
    folder_objs = path_dataset_3D+curr_class+"/"
    files_objs  = os.listdir(folder_objs)
    for obj_name in files_objs:
        print(f"Creating Multiview ({total_objs}): {obj_name}")
        
        # Load Object
        path_curr_obj = folder_objs + obj_name + '/' + "models/model_normalized.obj"
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
            output_filename = obj_name + f"_{idx}.jpg"
            output_folder_path = f"{path_dataset_multiview}{curr_class}/"
            screenshot(output_folder_path+output_filename)
            print(f"({total_objs}) {output_folder_path+output_filename}")
        
        total_objs += 1

        # # Stop if necessary (Debug Only)
        # if total_objs >= 3:
        #     exit(-1)