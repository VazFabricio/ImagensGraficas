import pygame
from OpenGL.GL import *


def load_texture(image_path, scale):
    image_surface = pygame.image.load(image_path).convert_alpha()
    image_surface = pygame.transform.scale(image_surface, scale)
    image_data = pygame.image.tostring(image_surface, "RGBA", True)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_surface.get_width(), image_surface.get_height(), 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

