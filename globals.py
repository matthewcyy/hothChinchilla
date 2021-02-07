"""
Globals
"""
import pygame

textcolor = (255, 255, 255)
bgcolor = (0, 0, 0)
red = (255, 0, 0)
margin = 5
max_shift = 13
font_size = 20
pygame.font.init()
font = pygame.font.SysFont("Menlo", font_size)


def write(screen, location, text, color=textcolor):
    text_surf = font.render(text, True, color)
    return screen.blit(text_surf, text_surf.get_rect(center=location))
