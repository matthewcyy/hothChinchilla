import math
import pygame
import random


# Asteroids have a random X coordinate and start at the top of the screen(can be changed)
# They have a random angle of velocity between 0 and 180 degrees
# The magnitude of velocity can be changed for each asteroid
class Asteroid:
    def __init__(self, velocity):
        self.asteroidImg = pygame.image.load('Asteroids.png')
        self.asteroidX = random.randint(200, 400)
        self.asteroidY = 0
        self.asteroidVelocity = velocity
        self.asteroidAngle = random.uniform(0, math.pi)

    # makes the asteroid move on its own
    @staticmethod
    def move(self):
        self.asteroidX += self.asteroidVelocity * math.cos(self.asteroidAngle)
        self.asteroidY += self.asteroidVelocity * math.sin(self.asteroidAngle)
        if self.asteroidX > 600 or self.asteroidX < 0 or self.asteroidY > 400 or self.asteroidY < 0:
            del self

    # the asteroid will delete itself if the laser is within 20 pixels of its center
    @staticmethod
    def destroy(self, laserx, lasery):
        distance = math.sqrt(math.pow(laserx - self.asteroidX, 2) + math.pow(lasery - self.asteroidY, 2))
        if distance < 20:
            del self
        else:
            del self

    # returns true if the asteroid collides with the player and false if it does not
    @staticmethod
    def collide(self, playerx, playery):
        distance = math.sqrt(math.pow(playerx - self.asteroidX, 2) + math.pow(playery - self.asteroidY, 2))
        if distance < 20:
            return True
        else:
            return False
