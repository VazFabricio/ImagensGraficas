import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from constants import *


def screen_config_start():
    display = (DISPLAY_HEIGHT, DISPLAY_WIDTH)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)


def projection_matrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (DISPLAY[0] / DISPLAY[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

