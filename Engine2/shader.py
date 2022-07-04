from glapp.PyOGLApp import *
import numpy as np
from glapp.Utils import *
from glapp.GraphicsData import *
from glapp.Square import *

vertex_shader = r'''
#version 330 core
in vec3 pos;
in vec3 vertex_color;
uniform vec3 translation;
out vec3 color;
void main() 
{
    vec3 pos = pos + translation;
    gl_Position = vec4(pos, 1);
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
        self.square = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-1,1,0))

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.square.draw()

FirstShader().mainloop()
