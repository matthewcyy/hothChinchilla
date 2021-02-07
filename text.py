"""
To hold encrypted text
"""

import pygame
import sys
import string
import random
from ciphers import caesar_cipher
from displayshift import DisplayBox
from globals import *
pygame.init()


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
    from displayshift import CaesarShiftDisplay

    size = width, height = 500, 500

    surface = pygame.display.set_mode(size)
    # hangmantext = HangmanSpace("g A h!", surface, 50, 50)
    display = CaesarShiftDisplay(surface, 350, 50, 100, 33)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(display)
    # sprite_group.add(hangmantext)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                private_key_shift = int(event.key) - int(pygame.K_0)
                if event.key == pygame.K_SEMICOLON:
                    # hangmantext.reveal_letter()
                    pass
                elif event.key == pygame.K_LEFTBRACKET:
                    display.update(-1)
                    #hangmantext.apply_private_key(display.get_shift())
                    #hangmantext.update()
                elif event.key == pygame.K_RIGHTBRACKET:
                    display.update(1)
                    #hangmantext.apply_private_key(display.get_shift())
                    #hangmantext.update()

        surface.fill(bgcolor)
        sprite_group.draw(surface)
        pygame.display.flip()
