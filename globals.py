"""
Globals
words.txt taken from MITx 6.00.1x Introduction to Computer Science and Programming Using Python
"""
import pygame

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KEYBOARD_BG = (24, 24, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
margin = 5
max_shift = 13
font_size = 20
pygame.font.init()
font = pygame.font.SysFont("Menlo", font_size)


def write(screen, location, text, color=WHITE):
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, text_surf.get_rect(center=location))


def load_words(file_name):
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    in_file.close()
    return word_list


def filter_len(words, max_len=4, min_len=4):
    return list(filter(lambda x: min_len <= len(x) <= max_len, words))
