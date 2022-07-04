from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *

vertex_shader = r'''
#version 330 core
in vec3 pos;
void main() 
{
    gl_Position = vec4(pos.x, pos.y, pos.z, 1);
}
'''

fragment_shader = r'''
#version 330 core
out vec4 frag_color;
void main() 
{
    frag_color = vec4(1, 0, 0, 1);
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


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)

FirstShader().mainloop()
