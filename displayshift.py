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


def write(screen, text, location, color=textboxcolor):
    return screen.blit(font.render(text, True, color), location)


class CaesarShiftDisplay(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((left + width, top + height))
        self.image.fill(bgcolor)
        self.rectangle = pygame.Rect(left, top, width, height)
        self.margin_rect = pygame.Rect(left + 1, top + 1, width - 2, height - 2)
        pygame.draw.rect(self.image, textboxcolor, self.rectangle, width=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = (left, top)
        self.shift = 0
        self.text_loc = ((left + width) / 2 + font_size, (top + height) / 2 + font_size)
        write(self.image, str(self.shift), self.text_loc)

    def update(self, shift):
        if abs(self.shift + shift) > max_shift:
            return
        pygame.sprite.Sprite.update(self)
        self.shift += shift
        self.image.fill(bgcolor, self.margin_rect)
        write(self.image, str(self.shift), self.text_loc)


if __name__ == "__main__":
    size = width, height = 500, 500

    surface = pygame.display.set_mode(size)
    left, top = 50, 50
    display = CaesarShiftDisplay(left, top, 100, 50)
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
