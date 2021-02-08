"""
Chinchilla main.py
"""

# import libraries
import pygame
import random
from globals import *
from displayshift import CaesarShiftDisplay, HangmanSpace
from healthbar import Lives
# pygame initialization
pygame.init()

# framework
scale = 2
size = (375 * scale, 667 * scale)
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

MAX_WORD_LEN = 7
MIN_WORD_LEN = 3
word_list = load_words("words.txt")
word_list = filter_len(word_list, MAX_WORD_LEN, MIN_WORD_LEN)
word = random.choice(word_list)

play_area_size = (375 * scale, 525 * scale)  # (750, 1050)
play_area_height = -100 * scale
play_area_height2 = -650 * scale
play_area_height3 = -1200 * scale

hangmantext = HangmanSpace(word, screen,
                           play_area_size[0] // 2 - scale * (font_size + 5) * len(word),
                           play_area_size[1] + scale * 50)
code_loc = list(hangmantext.center)
code_loc[1] -= 30

caesar_width, caesar_height = 100, (font_size + 10)
display = CaesarShiftDisplay(screen,
                             play_area_size[0] // 2 + scale * (font_size + 5) * len(word) - caesar_width,
                             play_area_size[1] + scale * 50,
                             caesar_width, caesar_height)
shift_loc = list(display.center)
shift_loc[1] -= 30

healthbar = Lives(screen, play_area_size[0] // 2, play_area_size[1] + scale * 100, 5, font_size)
lives_loc = list(healthbar.hearts[0].topleft)
lives_loc[0] -= (font_size * 2)
lives_loc[1] += healthbar.hearts[0].size // 2

# manage fps
clock = pygame.time.Clock()

# ~~~~ Game loop initialization ~~~~
gameRunning = True

# ------------- Main program ---------------
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
            break
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

    # play area
    play_area = pygame.image.load("space.jpg")
    play_area = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1]+100))
    play_area2 = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1]+100))
    play_area3 = pygame.transform.scale(play_area, (play_area_size[0], play_area_size[1] + 100))

    for counter in range(2):
        play_area_height += 2
        play_area_height2 += 2
    if play_area_height > size[1] - 150 * scale:
        play_area_height = -600 * scale
    elif play_area_height2 > size[1] - 150 * scale:
        play_area_height2 = -600 * scale

    screen.blit(play_area, (0, play_area_height))
    screen.blit(play_area2, (0, play_area_height2))
    screen.blit(play_area3, (0, play_area_height3))

    # keyboard area
    keyboard_area = pygame.Rect(0, play_area_size[1], play_area_size[0],  play_area_size[1] - 55 * scale)
    pygame.draw.rect(screen, KEYBOARD_BG, keyboard_area)
    write(screen, shift_loc, "SHIFT:")
    display.draw()
    write(screen, code_loc, "CODE:")
    hangmantext.draw()
    write(screen, lives_loc, "LIVES:")
    healthbar.draw()

    # refresh screen at 60fps
    SpriteList.update()
    SpriteList.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
