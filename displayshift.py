"""
Text box to solve encrypted text with caesar cipher in pygame
pygame 2.0.1
"""

import sys
import pygame
from globals import *
pygame.init()


class DisplayBox(pygame.sprite.Sprite):
    def __init__(self, screen, left, top, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(screen.get_size())
        self.image.fill(bgcolor)
        self.rectangle = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self.image, textcolor, self.rectangle, width=1)
        self.rect = self.image.get_rect()
        self.topleft = (left, top)
        self.center = (left + width / 2, top + height / 2)

    def redraw(self):
        pygame.draw.rect(self.image, bgcolor, self.rectangle)
        pygame.draw.rect(self.image, textcolor, self.rectangle, width=1)


class CaesarShiftDisplay(DisplayBox):
    def __init__(self, screen, left, top, width, height):
        super().__init__(screen, left, top, width, height)
        self.shift = 0
        write(self.image, self.center, str(self.shift))

    def get_shift(self):
        return self.shift

    def update(self, shift):
        if abs(self.shift + shift) > max_shift:
            return
        pygame.sprite.Sprite.update(self)
        self.shift += shift
        self.redraw()
        write(self.image, self.center, str(self.shift))


if __name__ == "__main__":
    size = width, height = 250, 500
    surface = pygame.display.set_mode(size)
    left, top = 120, 360
    display = CaesarShiftDisplay(surface, left, top, 100, 33)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(display)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFTBRACKET:
                    display.update(-1)
                elif event.key == pygame.K_RIGHTBRACKET:
                    display.update(1)

        surface.fill(bgcolor)
        sprite_group.draw(surface)
        pygame.display.flip()
