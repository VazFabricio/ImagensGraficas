import random
from screen import *
from images import *

pygame.init()

screen_config_start()

texture_square = load_texture("nave.png", (50, 50))

texture_rectangle = load_texture("plataforma.png", (0.2, 0.2))

texture_background = load_texture("fundo2.png", DISPLAY)


def draw_background(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-5, -4, 0)
    glTexCoord2f(1, 0)
    glVertex3f(5, -4, 0.0)
    glTexCoord2f(1, 1)
    glVertex3f(5, 4, 0.0)
    glTexCoord2f(0, 1)
    glVertex3f(-5, 4, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_square(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(X_SHIP, Y_SHIP, 0.0)
    glTexCoord2f(1, 0)
    glVertex3f(X_SHIP + 0.5, Y_SHIP, 0.0)
    glTexCoord2f(1, 1)
    glVertex3f(X_SHIP + 0.5, Y_SHIP + 0.5, 0.0)
    glTexCoord2f(0, 1)
    glVertex3f(X_SHIP, Y_SHIP + 0.5, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_rectangle(pos_x, pos_y, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glVertex3f(pos_x, pos_y, 0.0)
    glVertex3f(pos_x + 1, pos_y, 0.0)
    glVertex3f(pos_x + 1, pos_y + 0.2, 0.0)
    glVertex3f(pos_x, pos_y + 0.2, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def check_collision():
    square_left = X_SHIP
    square_right = X_SHIP + 0.5
    square_top = Y_SHIP + 0.5
    square_bottom = Y_SHIP

    rect1_left = RANDOM_POSITIONS[0]
    rect1_right = RANDOM_POSITIONS[0] + 1
    rect1_top = RANDOM_POSITIONS[1] + 0.2
    rect1_bottom = RANDOM_POSITIONS[1]

    rect2_left = RANDOM_POSITIONS[2]
    rect2_right = RANDOM_POSITIONS[2] + 1
    rect2_top = RANDOM_POSITIONS[3] + 0.2
    rect2_bottom = RANDOM_POSITIONS[3]

    if (square_right >= rect1_left and square_left <= rect1_right and
        square_bottom <= rect1_top and square_top >= rect1_bottom) or \
            (square_right >= rect2_left and square_left <= rect2_right and
             square_bottom <= rect2_top and square_top >= rect2_bottom):
        return True
    else:
        return False


while True:

    glClearColor(BACK_RED, BACK_GREEN, BACK_BLUE, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MOVING_LEFT = True
            elif event.key == pygame.K_RIGHT:
                MOVING_RIGHT = True
            elif event.key == pygame.K_UP:
                MOVING_UP = True
            elif event.key == pygame.K_DOWN:
                MOVING_DOWN = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                MOVING_LEFT = False
            elif event.key == pygame.K_RIGHT:
                MOVING_RIGHT = False
            elif event.key == pygame.K_UP:
                MOVING_UP = False
            elif event.key == pygame.K_DOWN:
                MOVING_DOWN = False

    if MOVING_LEFT and X_SHIP > -4:
        X_SHIP -= 0.05
    if MOVING_RIGHT and X_SHIP < 3.5:
        X_SHIP += 0.05
    if MOVING_UP and Y_SHIP < 2:
        Y_SHIP += 0.05
    if MOVING_DOWN and Y_SHIP > -2.5:
        Y_SHIP -= 0.05

    RANDOM_POSITIONS[1] -= SPEED
    RANDOM_POSITIONS[3] -= SPEED

    if RANDOM_POSITIONS[1] <= -3.0:
        RANDOM_POSITIONS[1] = random.randrange(4, 5)
        RANDOM_POSITIONS[0] = random.randrange(-4, 4)
        COLLISION_DETECTED = False

    if RANDOM_POSITIONS[3] <= -3.0:
        RANDOM_POSITIONS[3] = random.randrange(4, 5)
        RANDOM_POSITIONS[2] = random.randrange(-4, 4)
        COLLISION_DETECTED = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Configura a matriz MVP
    projection_matrix()

    draw_background(texture_background)

    draw_square(texture_square)

    draw_rectangle(RANDOM_POSITIONS[0], RANDOM_POSITIONS[1], texture_rectangle)

    draw_rectangle(RANDOM_POSITIONS[2], RANDOM_POSITIONS[3], texture_rectangle)

    if not COLLISION_DETECTED and check_collision():
        print("Colisão detectada!")
        COLLISION_DETECTED = True
        BACK_RED += 0.1
        BACK_GREEN -= 0.1
        NUMBER_OF_COLLISIONS += 1
        SPEED += 0.005
        if NUMBER_OF_COLLISIONS == 10:
            quit()

    pygame.display.flip()
    pygame.time.wait(10)
