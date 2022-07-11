import pygame
from OpenGL.GLU import *
from math import *
import numpy as np
from .Transformations import *
from .Uniform import *

class Camera:
    def __init__(self, program_id, w, h):
        self.transformation = identity_mat()
        self.transformation[2][3] = 6;
        self.transformation[1][3] = 2;
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.1
        self.projection_mat = self.perspective_mat(60, w/h, 0.01, 10000)
        self.projection = Uniform("mat4", self.projection_mat)
        self.projection.find_variable(program_id, "projection_mat")
        self.program_id = program_id
        self.screen_width = w
        self.screen_height = h

    def perspective_mat(self, angle_of_view, aspect_ratio, near_plane, far_plane):
        view_angle = radians(angle_of_view)
        d = 1.0 / tan(view_angle/2)
        r = aspect_ratio
        b = (far_plane + near_plane) / (near_plane - far_plane)
        c = (far_plane * near_plane) / (near_plane - far_plane)
        return np.array([[d/r, 0, 0, 0],
                        [0, d, 0, 0],
                        [0, 0, b, c],
                        [0, 0, -1, 0]], np.float32)

    def rotate(self, yaw, pitch):
        forward = pygame.Vector3(self.transformation[0, 2], self.transformation[1, 2], self.transformation[2, 2])
        up = pygame.Vector3(0, 1, 0)
        angle = forward.angle_to(up)
        self.transformation = rotate(self.transformation, yaw, 'y', False)

        # account for gimbal lock
        if angle < 170 and pitch > 0 or angle > 30 and pitch < 0:
            self.transformation = rotate(self.transformation, pitch, 'x', True)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(self.screen_width/2, self.screen_height/2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.transformation = translate(self.transformation, 0, 0, self.key_sensitivity)
        if keys[pygame.K_w]:
            self.transformation = translate(self.transformation, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_a]:
            self.transformation = translate(self.transformation, -self.key_sensitivity, 0, 0)
        if keys[pygame.K_d]:
            self.transformation = translate(self.transformation, self.key_sensitivity, 0, 0)

        self.projection.load()
        lookat_mat = self.transformation
        lookat = Uniform("mat4", lookat_mat)
        lookat.find_variable(self.program_id, "view_mat")
        lookat.load()
