import pygame, random
import settings, object

class Territory(object.GameObject):
    def __init__(self, location, height, length, territory):
        super().__init__()
        self.location = location
        self.height = height
        self.length = length
        self.territory = territory
