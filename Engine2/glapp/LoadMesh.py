import random
from .AnimatingMesh import *
import pygame
from .Utils import *
from .Transformations import *

class LoadMesh(AnimatingMesh):
    def __init__(self, filename, program_id, draw_type=GL_TRIANGLES,
                 location=pygame.Vector3(0, 0, 0),
                 rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 scale=pygame.Vector3(1, 1, 1),
                 move_rotation=Rotation(0, pygame.Vector3(0, 1, 0))):

        vertices, triangles, uvs, uvs_indices, normals, normal_indices = self.load_drawing(filename)
        vertices = format_vertices(vertices, triangles)
        vertex_normals = format_vertices(normals, normal_indices)
        vertex_uvs = format_vertices(uvs, uvs_indices)
        # colors = np.random.uniform(low=0.0, high=1.0, size=(len(vertices), 3)).astype("float32")
        colors = []
        # colors.append([[1, 1, 1]] * len(vertices))
        for i in range(len(vertices)):
            colors.append(1)
            colors.append(1)
            colors.append(1)
        super().__init__(program_id, vertices, vertex_normals, vertex_uvs, colors, draw_type, location, rotation, scale, move_rotation=move_rotation)

    def load_drawing(self, filename):
        vertices = []
        triangles= []
        normals = []
        uvs = []
        uvs_indices = []
        normal_indices = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "vn":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    normals.append((vx, vy, vz))
                if line[:2] == "vt":
                    vx, vy = [float(value) for value in line[3:].split()]
                    uvs.append((vx, vy))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)

                    uvs_indices.append([int(value) for value in t1.split('/')][1] - 1)
                    uvs_indices.append([int(value) for value in t2.split('/')][1] - 1)
                    uvs_indices.append([int(value) for value in t3.split('/')][1] - 1)

                    normal_indices.append([int(value) for value in t1.split('/')][2] - 1)
                    normal_indices.append([int(value) for value in t2.split('/')][2] - 1)
                    normal_indices.append([int(value) for value in t3.split('/')][2] - 1)
                line = fp.readline()

        return vertices, triangles, uvs, uvs_indices, normals, normal_indices
