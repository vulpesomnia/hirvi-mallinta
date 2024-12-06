import pygame, random
import settings, object, moose

class Territory(object.GameObject):
    def __init__(self, location, radius, mooseNumber):
        super().__init__()
        self.location = location
        self.radius = radius
        self.population = []
        for _ in range(mooseNumber):
            randDir = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)))
            self.population.append(moose.Moose(self.location + randDir * random.uniform(0, radius), random.uniform(1.7, 2.1), random.uniform(2.5, 3) * settings.PIXELS_PER_METER, self))
