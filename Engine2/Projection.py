from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *
from glapp.Square import *
from glapp.Axes import *

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

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-1,1,0))
        self.axis = Axes(self.program_id)
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        self.square.draw()
        self.axis.draw()

Projection().mainloop()
