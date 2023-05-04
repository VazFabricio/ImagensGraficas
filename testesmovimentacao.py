import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (640, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)


def draw_line(x, y, r, g, b):
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x, y)
    glColor3f(r, g, b)
    glEnd()


def draw_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_square():
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0.0)
    glVertex3f(1, 0, 0.0)
    glVertex3f(1, 1, 0.0)
    glVertex3f(0, 1, 0.0)
    glEnd()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Configura a matriz MVP
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    #draw_point()

    draw_line(10, 0, 1, 0, 0)
    draw_line(0, 10, 0, 1, 0)
    draw_line(-10, 0, 0, 0, 1)
    draw_line(0, -10, 0, 1, 1)

    draw_point(1, 1)
    draw_point(-1, -1)

    pygame.display.flip()
    pygame.time.wait(10)
