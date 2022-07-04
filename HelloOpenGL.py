import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in python")

# orthographic projection: used for 2d
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 480, 0)

def draw_start(x, y, size):
    glPointSize(size)
    glBegin()
    glVertex2i(x, y)
    glEnd()

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # draw a point
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glEnd()

    glPointSize(15)
    glBegin(GL_POINTS)
    glVertex2i(110, 60)
    glVertex2i(130, 70)
    glEnd()

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(150, 80)
    glVertex2i(220, 150)
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2i(228, 160)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()