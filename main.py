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

player_x_speed = 0
player_y_speed = 0

# spaceship class
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([120, 120])
        self.image.fill(RED)
        self.image = pygame.image.load("ship.png")
        #sets spaceship size
        self.image = pygame.transform.smoothscale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 200, 20
    def update(self):
        self.rect.x += player_x_speed
        self.rect.y += player_y_speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship_x_pos, ship_y_pos):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ship_x_pos+50, ship_y_pos-15
    def update(self):
        #bullet momentum continues
        self.rect.y -= 8

#group initialization
BulletList = pygame.sprite.Group()
SpriteList = pygame.sprite.Group()

player = Ship()
#adds player spaceship to list of active sprites
SpriteList.add(player)

#manage fps
clock = pygame.time.Clock()

#~~~~ Game loop initialization ~~~~
gameRunning = True

#------------- Main program ---------------
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #new instance of bullet created when spacebar pressed
                new_bullet = Bullet(player.rect.x, player.rect.y)
                #added to list of active bullets
                BulletList.add(new_bullet)
                SpriteList.add(new_bullet)
            elif event.key == pygame.K_RIGHT:
                #player spaceshp moves right
                player_x_speed = 5
            elif event.key == pygame.K_LEFT:
                player_x_speed = -5
            elif event.key == pygame.K_UP:
                player_y_speed = -5
            elif event.key == pygame.K_DOWN:
                player_y_speed = 5
        if event.type == pygame.KEYUP:
            #player stops moving in direction
            if event.key == pygame.K_RIGHT:
                player_x_speed = 0
            elif event.key == pygame.K_LEFT:
                player_x_speed = 0
            elif event.key == pygame.K_UP:
                player_y_speed = 0
            elif event.key == pygame.K_DOWN:
                player_y_speed = 0

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

    SpriteList.update()
    SpriteList.draw(screen)
    #refresh screen at 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()