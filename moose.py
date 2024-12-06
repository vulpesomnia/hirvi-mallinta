import pygame
import settings, object

class Moose(object.GameObject):# Korkeus, pituus, reviiri
    def __init__(self, location, height, length, territory):
        super().__init__()
        self.location = location
        self.height = height
        self.length = territory
        self.territory = territory

    def fixed_tick(self, dt):
        self.location = self.location.lerp(settings.world_to_screen((0,0)), 0.02*dt)
