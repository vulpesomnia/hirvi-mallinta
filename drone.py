import pygame
import settings, object

class Drone(object.GameObject):
    def __init__(self, location, velocity, height):
        super().__init__()
        self.location = location
        self.velocity = velocity
        self.height = height
        self.sight = 400 * settings.PIXELS_PER_METER
        self.sprite = object.Sprite(pygame.Vector2(self.sight/settings.PIXELS_PER_METER, 1), (255, 0, 255, 50), self.location)
