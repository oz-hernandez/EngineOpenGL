from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *

vertex_shader = r'''
#version 330 core
in vec3 pos;
in vec3 vertex_color;
out vec3 color;
void main() 
{
    gl_Position = vec4(pos.x, pos.y, pos.z, 1);
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

class FirstShader(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.vao_ref = None
        self.vertex_count = 0

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        glPointSize(10)
        position_data = [[0, -0.9, 0],
                         [-0.6, 0.8, 0],
                         [0.9, -0.2, 0],
                         [-0.9, -0.2, 0],
                         [0.6, 0.8, 0]]
        self.vertex_count = len(position_data)
        position_variable = GraphicsData("vec3", position_data)
        position_variable.create_variable(self.program_id, "pos")
        color_data = [[1, 0 ,0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 0]]
        color_var = GraphicsData("vec3", color_data)
        color_var.create_variable(self.program_id, "vertex_color")


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, self.vertex_count)

FirstShader().mainloop()
