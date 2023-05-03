import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

pygame.init()
display = (640, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)


# Função para desenhar um quadrado
def draw_square():
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0.0)
    glVertex3f(0.2, 0, 0.0)
    glVertex3f(0.2, 1, 0.0)
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
    # Desenha um quadrado na posição (0,0,0)
    draw_square()

    glTranslatef(0.2, 1, 0)
    glRotatef(60, 1, 0, 0)
    draw_square()

    pygame.display.flip()
    pygame.time.wait(10)
