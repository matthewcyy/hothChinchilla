"""
Lives
"""

import pygame
import sys
from globals import *
pygame.init()

margin = 10  # px


class Heart:
    def __init__(self, screen, x, y, size=20):
        self.image = pygame.image.load("heart.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.topleft = x, y
        self.size = size
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.topleft)


class Lives:
    def __init__(self, screen, x, y, num_lives, heart_size=20):
        self.hearts = [Heart(screen, x + heart_size * i + margin, y, heart_size) for i in range(num_lives)]

    def lose_life(self):
        self.hearts.pop(-1)

    def num_lives(self):
        return len(self.hearts)

    def draw(self):
        for heart in self.hearts:
            heart.draw()


if __name__ == "__main__":
    gameRunning = True
    size = width, height = 200, 200
    surface = pygame.display.set_mode(size)
    lives = Lives(surface, 30, 20, 7)

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
                break
            # replace this with the signal the asteroid sends out
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lives.lose_life()
                    if lives.num_lives() <= 0:
                        gameRunning = False

        surface.fill(BLACK)
        lives.draw()
        pygame.display.flip()
    pygame.quit()
