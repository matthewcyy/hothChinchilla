import math
import pygame
import random


# Asteroids have a random X coordinate and start at the top of the screen(can be changed)
# They have a random angle of velocity between 0 and 180 degrees
# The magnitude of velocity can be changed for each asteroid
# The asteroid contains an encrypted value
class Asteroid:
    def __init__(self, velocity, value):
        self.asteroidX = random.randint(200, 400)
        self.asteroidY = 0
        self.asteroidVelocity = velocity
        self.asteroidAngle = random.uniform(0, math.pi)
        self.asteroidValue = value
        if random.randint(0, 10) == 10:
            self.special = True
            self.asteroidImg = pygame.image.load('specialAsteroid.png')
        else:
            self.special = False
            self.asteroidImg = pygame.image.load('Asteroids.png')

    # makes the asteroid move on its own in its predetermined direction
    @staticmethod
    def move(self):
        self.asteroidX += self.asteroidVelocity * math.cos(self.asteroidAngle)
        self.asteroidY += self.asteroidVelocity * math.sin(self.asteroidAngle)
        if self.asteroidX > 600 or self.asteroidX < 0 or self.asteroidY > 400 or self.asteroidY < 0:
            del self

    # the asteroid will delete itself if the laser is within 20 pixels of its center and return its value
    @staticmethod
    def destroy(self, laserx, lasery):
        distance = math.sqrt(math.pow(laserx - self.asteroidX, 2) + math.pow(lasery - self.asteroidY, 2))
        if distance < 20:
            del self
            if self.special:
                return self.asteroidValue   # this will need to be changed to decrypt the encryption
            else:
                return self.asteroidValue

    # returns true if the asteroid collides with the player and false if it does not
    @staticmethod
    def collide(self, playerx, playery):
        distance = math.sqrt(math.pow(playerx - self.asteroidX, 2) + math.pow(playery - self.asteroidY, 2))
        if distance < 20:
            return True
        else:
            return False
