import pygame

from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *
from glapp.Square import *
from glapp.Axes import *
from glapp.Cube import *
from glapp.LoadMesh import *

vertex_shader = r'''
#version 330 core
in vec3 pos;
in vec3 vertex_color;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 color;
void main() 
{
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(pos, 1);
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
out vec4 frag_color;
void main() 
{
    frag_color = vec4(color, 1);
}
'''

class Projection(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.square = None
        self.axis = None
        self.cube = None
        self.teapot = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.axis = Axes(self.program_id)
        self.cube = Cube(self.program_id,
                         move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        self.teapot = LoadMesh("models/teapot.obj", self.program_id,
                               scale=pygame.Vector3(1, 1, 1),
                               move_rotation=Rotation(1, pygame.Vector3(0, 1, 0)))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        self.axis.draw()
        self.cube.draw()

Projection().mainloop()
