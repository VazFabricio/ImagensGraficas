import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set the width and height of the screen (width, height)
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the caption for the window
pygame.display.set_caption("Particle System")


# Define a particle class
class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(10, 20)
        self.velocity = [random.randint(-5, 5), random.randint(-5, 5)]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] < 0 or self.pos[1] > size[1]:
            self.velocity[1] = -self.velocity[1]


# Create a list to hold the particles
particles = []

# Main program loop
done = False
clock = pygame.time.Clock()

while not done:
    # --- Main Event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Create a new particle on mouse click
        elif event.type == pygame.MOUSEMOTION:
            particles.append(Particle(list(event.pos)))

    # --- Game logic goes here ---
    for particle in particles:
        particle.update()

    # --- Drawing code goes here --
    screen.fill(BLACK)

    for particle in particles:
        particle.draw(screen)

    # --- Update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit
pygame.quit()
