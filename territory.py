import pygame, random
import settings, object, moose

class Territory(object.GameObject):
    def __init__(self, location, radius, mooseNumber):
        super().__init__()
        self.location = location
        self.radius = radius
        self.population = []
        randDir = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))) * random.uniform(0, radius)
        for n in range(mooseNumber):
            xOffset = pygame.Vector2(n*5*settings.PIXELS_PER_METER, 0)
            if n > 0:
                self.population.append(moose.Moose(self.population[0].location - xOffset, random.uniform(settings.MIN_MOOSE_HEIGHT, settings.MAX_MOOSE_HEIGHT), random.uniform(settings.MIN_MOOSE_LENGTH, settings.MAX_MOOSE_LENGTH) * settings.PIXELS_PER_METER, self, self.population[n-1]))
            else:
                self.population.append(moose.Moose(self.location + randDir , random.uniform(1.7, 2.1), random.uniform(2.5, 3) * settings.PIXELS_PER_METER, self))
        self.sprite = object.Sprite(pygame.Vector2(radius*2, radius*2), (0, 255, 126, 50), self.location)
        pygame.draw.circle(self.sprite.rect, (255, 255, 255), (radius, radius), radius)
