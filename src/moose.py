import pygame
import random

import settings
import object

epsilonVector = pygame.Vector2(0.0001, 0.0001)

class Moose(object.GameObject):
    def __init__(self, location, length, territory, following = None):
        super().__init__()
        self.location = location
        self.length = length
        self.territory = territory
        self.following = following
        self.resting = False
        self.colliding = False
        self.sprite = object.Sprite(pygame.Vector2(self.length*2, self.length), (255, 100, 0), self.location)

        if self.following is not None:
            self.target = self.following
            self.targetDistance = random.uniform(5, 10)
        else:
            self.targetLocation = location

        self.time = 0
        self.speed = settings.MOOSE_SPEED

    def fixed_tick(self, dt):
        if not self.resting:
            # Checks if is leader or not
            if self.following is not None:
                self.velocity = pygame.Vector2.normalize(self.target.location - self.location + epsilonVector) * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
                if settings.get_square_distance(self.location, self.target.location) >= self.targetDistance**2 * settings.PIXELS_PER_METER:
                    self.location += self.velocity * dt
            else:
                self.velocity = pygame.Vector2.normalize(self.targetLocation - self.location + epsilonVector) * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED

            if self.following is None:
                if settings.get_square_distance(self.location, self.targetLocation) >= 1 * settings.PIXELS_PER_METER:
                    self.location += self.velocity * dt
                else:
                    randDir = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) + epsilonVector)
                    self.targetLocation = self.territory.location + randDir * random.uniform(0, self.territory.radius - 5 * settings.PIXELS_PER_METER)

            for i in range(len(self.territory.population)):
                if self.territory.population[i] != self:
                    if settings.get_square_distance(self.territory.population[i].location, self.location) <= (self.territory.population[i].length + 4)**2 * settings.PIXELS_PER_METER:
                        dir = pygame.Vector2.normalize(self.territory.population[i].location - self.location + epsilonVector)
                        self.territory.population[i].location += dir * 2 * settings.PIXELS_PER_METER
