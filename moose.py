import pygame
import settings, object

class Moose(object.GameObject):# Korkeus, pituus, reviiri
    def __init__(self, location, height, length, territory):
        super().__init__()
        self.location = location
        self.height = height
        self.length = length
        self.territory = territory
        self.sprite = object.Sprite(pygame.Vector2(self.length*2, self.length), (255, 100, 0), self.location)

    def fixed_tick(self, dt):
        self.location += pygame.Vector2(2*settings.TICK_SPEED * settings.PIXELS_PER_METER * dt, 0)
