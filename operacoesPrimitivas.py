import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()
display = (640, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)


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
    """Matriz de Projeção: É usada para projetar objetos em um espaço tridimensional
        em uma tela bidimensional. A matriz de projeção define a perspectiva da cena e
        pode ser definida no OpenGL usando a função"""
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    """É usada para transformar objetos em um espaço de coordenadas
        de mundo para um espaço de coordenadas de visão. Isso inclui a rotação, escala e
        translação do objeto em relação ao observador."""
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    draw_square()

    glTranslatef(0.2, 1, 0)
    glRotatef(45, 0, 0, -1)
    glScalef(-1, 1, 1)
    draw_square()

    pygame.display.flip()
    pygame.time.wait(10)
