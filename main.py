#import libraries
import pygame
#pygame initialization
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#framework
size = (750, 1334)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chinchilla")

#~~~~ Game loop initialization ~~~~
gameRunning = True

#------------- Main program ---------------
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()