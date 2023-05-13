import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

pygame.init()
display = (720, 480)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)

x = 0.0
y = 0.0

rand_rec_x = 2
rand_rec_y = 2

moving_left = False
moving_right = False
moving_up = False
moving_down = False

collision_detected = False
number_of_collision = 0

back_red = 0.0
back_green = 1.0
back_blue = 0.0

random_positions = [2, 2, 2, 2]

speed = 0.06

# Carrega a imagem com canal alfa
image_surface_square = pygame.image.load("nave.png").convert_alpha()
image_surface_square = pygame.transform.scale(image_surface_square, (50, 50))
image_data_square = pygame.image.tostring(image_surface_square, "RGBA", True)

# Cria a textura OpenGL com canal alfa para o quadrado
texture_square = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_square)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_surface_square.get_width(), image_surface_square.get_height(), 0, GL_RGBA,
             GL_UNSIGNED_BYTE, image_data_square)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Carrega a imagem com canal alfa para os retângulos
image_surface_rectangle = pygame.image.load("plataforma.png").convert_alpha()
image_surface_rectangle = pygame.transform.scale(image_surface_rectangle, (100, 20))
image_data_rectangle = pygame.image.tostring(image_surface_rectangle, "RGBA", True)

# Cria a textura OpenGL com canal alfa para os retângulos
texture_rectangle = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_rectangle)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_surface_rectangle.get_width(), image_surface_rectangle.get_height(),
             0, GL_RGBA, GL_UNSIGNED_BYTE, image_data_rectangle)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)


def draw_square():
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_square)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(x, y, 0.0)
    glTexCoord2f(1, 0)
    glVertex3f(x + 0.5, y, 0.0)
    glTexCoord2f(1, 1)
    glVertex3f(x + 0.5, y + 0.5, 0.0)
    glTexCoord2f(0, 1)
    glVertex3f(x, y + 0.5, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_rectangle(pos_x, pos_y):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_rectangle)
    glBegin(GL_QUADS)
    glVertex3f(pos_x, pos_y, 0.0)
    glVertex3f(pos_x + 1, pos_y, 0.0)
    glVertex3f(pos_x + 1, pos_y + 0.2, 0.0)
    glVertex3f(pos_x, pos_y + 0.2, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def check_collision():
    square_left = x
    square_right = x + 0.5
    square_top = y + 0.5
    square_bottom = y

    rect1_left = random_positions[0]
    rect1_right = random_positions[0] + 1
    rect1_top = random_positions[1] + 0.2
    rect1_bottom = random_positions[1]

    rect2_left = random_positions[2]
    rect2_right = random_positions[2] + 1
    rect2_top = random_positions[3] + 0.2
    rect2_bottom = random_positions[3]

    if (square_right >= rect1_left and square_left <= rect1_right and
        square_bottom <= rect1_top and square_top >= rect1_bottom) or \
            (square_right >= rect2_left and square_left <= rect2_right and
             square_bottom <= rect2_top and square_top >= rect2_bottom):
        return True
    else:
        return False


while True:

    glClearColor(back_red, back_green, back_blue, 1)

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

    random_positions[1] -= speed
    random_positions[3] -= speed
    if random_positions[1] <= -3.0:
        random_positions[1] = random.randrange(4, 5)
        random_positions[0] = random.randrange(-4, 4)
        collision_detected = False

    if random_positions[3] <= -3.0:
        random_positions[3] = random.randrange(4, 5)
        random_positions[2] = random.randrange(-4, 4)
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

    draw_rectangle(random_positions[0], random_positions[1])

    draw_rectangle(random_positions[2], random_positions[3])

    if not collision_detected and check_collision():
        print("Colisão detectada!")
        collision_detected = True
        back_red += 0.1
        back_green -= 0.1
        number_of_collision += 1
        speed += 0.005
        if number_of_collision == 10:
            quit()

    pygame.display.flip()
    pygame.time.wait(10)
