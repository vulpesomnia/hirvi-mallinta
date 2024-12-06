import pygame, random
import settings, object

epsilonVector = pygame.Vector2(0.0001, 0.0001)

class Moose(object.GameObject):# Korkeus, pituus, reviiri
    def __init__(self, location, height, length, territory):
        super().__init__()
        self.location = location
        self.height = height
        self.length = length
        self.territory = territory
        self.colliding = False
        self.sprite = object.Sprite(pygame.Vector2(self.length*2, self.length), (255, 100, 0), self.location)
        self.targetLocation = location
        self.time = 0
        self.speed = 2

    def fixed_tick(self, dt):
        self.time += dt
        self.velocity = pygame.Vector2.normalize(self.targetLocation - self.location + epsilonVector) * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
        if settings.getDistance(self.location, self.targetLocation) >= 1 * settings.PIXELS_PER_METER:
            self.location += self.velocity * dt
        else:
            randDir = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) + epsilonVector)
            self.targetLocation = self.territory.location + randDir * random.uniform(0, self.territory.radius)
        for i in range(len(self.territory.population)):
            if self.territory.population[i] != self:
                if settings.getDistance(self.territory.population[i].location, self.location) <= 5 * settings.PIXELS_PER_METER:
                    dir = pygame.Vector2.normalize(self.territory.population[i].location - self.location + epsilonVector)
                    self.territory.population[i].location += dir * 2 * settings.PIXELS_PER_METER
