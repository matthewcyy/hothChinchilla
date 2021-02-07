"""
Text box to solve encrypted text with caesar cipher in pygame
pygame 2.0.1
"""

import sys
import pygame
import string
import random
from ciphers import caesar_cipher
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


class HangmanSpace(DisplayBox):
    def __init__(self, code: str, screen, left, top):
        width = (font_size + 5) * len(code)
        height = (font_size + 10)
        super().__init__(screen, left, top, width, height)
        self.code = code
        self.text = {}
        self.shift = random.randint(-max_shift, max_shift)

        # initialize to underscores separated by spaces if needed
        for letter in code:
            if letter in string.punctuation + ' ':
                self.text[letter] = letter
            else:
                self.text[letter] = '_'
        self.string = ' '.join([self.text[letter] for letter in code])
        write(self.image, self.center, self.string)

    def reveal_letter(self):
        """
        Destroyed the correct asteroid so randomly reveal a letter
        """
        idx = random.randint(0, len(self) - 1)
        letter = self.code[idx]
        self.text[letter] = caesar_cipher(letter, self.shift)
        self.string = ' '.join([self.text[letter] for letter in self.code])
        self.redraw()
        write(self.image, self.center, self.string)

    def apply_private_key(self, private_key_shift):
        self.string = ' '.join([self.text[letter] for letter in self.code])
        self.string = caesar_cipher(self.string, private_key_shift)
        self.redraw()
        write(self.image, self.center, self.string)

    def update(self):
        pygame.sprite.Sprite.update(self)
        # self.string = ' '.join([self.text[letter] for letter in self.code])
        self.redraw()
        write(self.image, self.center, self.string)

    def __len__(self):
        return len(self.code)


if __name__ == "__main__":
    size = width, height = 500, 500

    surface = pygame.display.set_mode(size)
    hangmantext = HangmanSpace("g A h!", surface, 50, 50)
    display = CaesarShiftDisplay(surface, 350, 50, 100, 33)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(hangmantext)
    sprite_group.add(display)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SEMICOLON:
                    hangmantext.reveal_letter()
                elif event.key == pygame.K_LEFTBRACKET:
                    display.update(-1)
                    hangmantext.apply_private_key(display.get_shift())
                    hangmantext.update()
                elif event.key == pygame.K_RIGHTBRACKET:
                    display.update(1)
                    hangmantext.apply_private_key(display.get_shift())
                    hangmantext.update()

        surface.fill(bgcolor)
        sprite_group.draw(surface)
        pygame.display.flip()
