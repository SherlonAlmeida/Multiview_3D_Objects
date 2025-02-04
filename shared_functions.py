# Download ModelNet10: https://www.kaggle.com/datasets/balraj98/modelnet10-princeton-3d-object-dataset?select=ModelNet10

"""
The following code uses VEDO and POLYSCOPE to open and visualize 3D objects, respectively.

Link to VEDO: https://vedo.embl.es/
Link to POLYSCOPE: https://polyscope.run/py/

Tutorials:
    -PART 1 - https://towardsdatascience.com/python-libraries-for-mesh-and-point-cloud-visualization-part-1-daa2af36de30
    -PART 2 - https://towardsdatascience.com/python-libraries-for-mesh-point-cloud-and-data-visualization-part-2-385f16188f0f
"""

from vedo import *      #Using VEDO to open 3D OBJ files
import polyscope as ps  #Using POLYSCOPE to visualize objects

"""Opens Object using VEDO"""
def load_object(filename):
    mesh = Mesh(filename,)
    return mesh

"""Rotates the object, given a mesh and an angle for X, Y and Z"""
def rotation(obj, ax=0, ay=0, az=0):
    #Rotate object in Z axis
    obj.rotate_x(ax, rad=False)
    obj.rotate_y(ay, rad=False)
    obj.rotate_z(az, rad=False)

    #Get object information
    faces = np.array(obj.cells) #mesh.faces()
    vertices = np.array(obj.vertices) #mesh.vertices()
    
    return faces, vertices

"""Center the object at Origin (0, 0, 0)"""
def center(vertices):
    center_coord = np.mean(vertices, axis=0)
    centered_vertices = vertices - center_coord
    return centered_vertices

"""
Description: generates a list with all the permutation of angles in (x, y, z)
Input:
    angle -> rotation applied after each iteration.
Output:
    rotations -> a list containing all the possible combinations in 3D,
    count -> total number of combinations performed.
"""
def combine_rotations_3D(angle = 45):
    count = 0
    rotations = []
    for x in range(0, 360, angle):
        for y in range(0, 360, angle):
            for z in range(0, 360, angle):
                rotations.append([x,y,z])
                count += 1
    print(f"{count} rotations were created combining (x, y, z)")
    return rotations, count