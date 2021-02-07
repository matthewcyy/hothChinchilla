"""
Text box to solve encrypted text with caesar cipher in pygame
pygame 2.0.1
"""

import sys
import pygame

pygame.init()
textboxcolor = (255, 255, 255)
bgcolor = (0, 0, 0)
margin = 5
max_shift = 13
font_size = 20
font = pygame.font.SysFont("Menlo", font_size)


def write(screen, rect, text, color=textboxcolor):
    text_surf = font.render(text, True, color)
    cx, cy = screen.get_rect().center
    return screen.blit(text_surf, text_surf.get_rect(center=rect.center))


class CaesarShiftDisplay(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2 * width, 2 * height))
        self.image.fill(bgcolor)
        self.rectangle = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self.image, textboxcolor, self.rectangle, width=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = (left, top)
        self.rect.center = (left + width / 2, top + height / 2)
        self.shift = 0
        write(self.image, self.rect, str(self.shift))

    def update(self, shift):
        if abs(self.shift + shift) > max_shift:
            return
        pygame.sprite.Sprite.update(self)
        self.shift += shift
        pygame.draw.rect(self.image, bgcolor, self.rectangle)
        pygame.draw.rect(self.image, textboxcolor, self.rectangle, width=1)
        write(self.image, self.rect, str(self.shift))


if __name__ == "__main__":
    size = width, height = 500, 500

    surface = pygame.display.set_mode(size)
    left, top = 40, 20
    display = CaesarShiftDisplay(left, top, 100, 33)
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
