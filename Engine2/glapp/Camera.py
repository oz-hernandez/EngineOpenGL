import pygame
from OpenGL.GLU import *
from math import *
import numpy as np
from .Transformations import *

class Camera:
    def __init__(self, program_id, w, h):
        self.transformation = identity_mat()
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.001
        self.projection_mat = self.perspective_mat(60, w/h, 0.01, 10000)

    def perspective_mat(self, angle_of_view, aspect_ratio, near_plane, far_plane):
        view_angle = radians(angle_of_view)
        d = 1.0 / tan(view_angle/2)
        r = aspect_ratio
        b = (far_plane + near_plane) / (near_plane - far_plane)
        c = (far_plane * near_plane) / (near_plane - far_plane)
        return np.array([d/r, 0, 0, 0],
                        [0, d, 0, 0],
                        [0, 0, b, c],
                        [0, 0, -1, 0], np.float32)

    def rotate(self, yaw, pitch):
        # self.yaw += yaw
        # self.pitch += pitch
        # self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        # self.forward.y = sin(radians(self.pitch))
        # self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        # self.foward = self.forward.normalize()
        # self.right = self.foward.cross(pygame.Vector3(0, 1, 0)).normalize()
        # self.up = self.right.cross(self.foward).normalize()

        self.transformation = rotate(self.transformation, yaw, 'y')
        self.transformation = rotate(self.transoformation, pitch, 'x')

    def update(self, w, h):
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(w/2, h/2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        # if self.pitch > 89.0:
        #     self.pitch = 89.0
        # if self.pitch < -89.0:
        #     self.pitch = -89.0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.transformation = translate(self.transformation, 0, 0, self.key_sensitivity)
        if keys[pygame.K_w]:
            self.transformation = translate(self.transformation, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_a]:
            self.transformation = translate(self.transformation, self.key_sensitivity, 0, 0)
        if keys[pygame.K_d]:
            self.transformation = translate(self.transformation, -self.key_sensitivity, 0, 0)
