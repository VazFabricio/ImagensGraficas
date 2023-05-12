import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

pygame.init()
display = (720, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

image = pygame.image.load("nave.png")

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)

x = 0.0
y = 0.0


def draw_square():
    glBegin(GL_QUADS)
    glVertex3f(x, y, 0.0)
    glVertex3f(x + 0.5, y, 0.0)
    glVertex3f(x + 0.5, y + 0.5, 0.0)
    glVertex3f(x, y + 0.5, 0.0)
    glEnd()


rand_x = 2
rand_y = 2


def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex3f(rand_x, rand_y, 0.0)
    glVertex3f(rand_x + 1, rand_y, 0.0)
    glVertex3f(rand_x + 1, rand_y + 0.2, 0.0)
    glVertex3f(rand_x + 0, rand_y + 0.2, 0.0)
    glEnd()


def check_collision():
    square_left = x
    square_right = x + 0.5
    square_top = y + 0.5
    square_bottom = y

    rect_left = rand_x
    rect_right = rand_x + 1
    rect_top = rand_y + 0.2
    rect_bottom = rand_y

    if square_left < rect_right and square_right > rect_left and square_bottom < rect_top and square_top > rect_bottom:
        return True
    else:
        return False


moving_left = False
moving_right = False
moving_up = False
moving_down = False

collision_detected = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_left and x > -4:
        x -= 0.05
    if moving_right and x < 3.5:
        x += 0.05
    if moving_up and y < 2:
        y += 0.05
    if moving_down and y > -2.5:
        y -= 0.05

    rand_y -= 0.05
    if rand_y <= -2.0:
        rand_y = random.randrange(4, 5)
        rand_x = random.randrange(-4, 4)
        collision_detected = False



    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Configura a matriz MVP
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)

    draw_square()

    draw_rectangle()

    if not collision_detected and check_collision():
        print("Colisão detectada!")
        collision_detected = True

    pygame.display.flip()
    pygame.time.wait(10)
