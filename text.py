"""
To hold encrypted text
"""

import pygame
import displayshift

pygame.init()


class HangmanSpace(pygame.sprite.Sprite):
    def __init__(self, spaces, code):
        pygame
        self.spaces = spaces
        self.code = code
