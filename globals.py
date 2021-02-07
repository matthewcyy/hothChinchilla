"""
Globals
"""
import pygame

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
