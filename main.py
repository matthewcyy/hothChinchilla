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

play_area_size = (750, 1050)
play_area_height = -200
play_area_height2 = -1300
play_area_height3 = -2400

#manage fps
clock = pygame.time.Clock()

#~~~~ Game loop initialization ~~~~
gameRunning = True


#------------- Main program ---------------
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False


    keyboard_img = pygame.image.load("keyboard.png")
    keyboard_img = pygame.transform.scale(keyboard_img, (750, 400))

    play_area = pygame.image.load("space.jpg")
    play_area2 = pygame.image.load("space2.jpg")
    play_area3 = pygame.image.load("space.jpg")
    play_area = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1]+100))
    play_area2 = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1]+100))
    play_area3 = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1] + 100))

    for counter in range(2):
        play_area_height += 2
        play_area_height2 += 2
    if play_area_height > size[1]-300:
        play_area_height = -1200
    elif play_area_height2 > size[1]-300:
        play_area_height2 = -1200

    screen.blit(play_area, (0, play_area_height))
    screen.blit(play_area2, (0, play_area_height2))
    screen.blit(play_area3, (0, play_area_height3))
    screen.blit(keyboard_img, (0, play_area_size[1] - 110))
    #refresh screen at 60fps
    pygame.display.flip()
    clock.tick(60)

pygame.quit()