from .Mesh import *

class Axes(Mesh):
    def __init__(self, program_id, location=pygame.Vector3(0, 0, 0)):
        vertices = [[-10, 0, 0],
                    [10, 0, 0],
                    [0, -10, 0],
                    [0, 10, 0],
                    [0, 0, -10],
                    [0, 0, 10]]

        colors = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]
        super().__init__(program_id, vertices, colors, GL_LINES, location)