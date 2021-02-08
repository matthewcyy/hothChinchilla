"""
Chinchilla main.py
"""

# import libraries
import pygame
import random
from globals import *
from displayshift import CaesarShiftDisplay, HangmanSpace
# pygame initialization
pygame.init()

# framework
scale = 1
size = (375 * scale, 667 * scale)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chinchilla")

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
caesar_width, caesar_height = 100, (font_size + 10)
display = CaesarShiftDisplay(screen,
                             play_area_size[0] // 2 + scale * (font_size + 5) * len(word) - caesar_width,
                             play_area_size[1] + scale * 50,
                             caesar_width, caesar_height)

# manage fps
clock = pygame.time.Clock()

# ~~~~ Game loop initialization ~~~~
gameRunning = True

# ------------- Main program ---------------
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

        # PLACEHOLDER FOR ASTEROID EVENTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SEMICOLON:
                hangmantext.reveal_letter()
            elif not hangmantext.revealed:
                continue
            elif event.key == pygame.K_LEFTBRACKET:
                display.update(-1)
                hangmantext.apply_private_key(display.get_shift())
                hangmantext.draw()
            elif event.key == pygame.K_RIGHTBRACKET:
                display.update(1)
                hangmantext.apply_private_key(display.get_shift())
                hangmantext.draw()

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
    display.draw()
    hangmantext.draw()

    # refresh screen at 60fps
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
