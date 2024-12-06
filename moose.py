import pygame, random
import settings, object

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
        self.speed = 10

    def fixed_tick(self, dt):
        self.time += dt
        if settings.getDistance(self.location, self.targetLocation) >= 1 * settings.PIXELS_PER_METER:
            self.location += self.direction * self.speed * settings.PIXELS_PER_METER * dt * settings.TICK_SPEED
        else:
            self.targetLocation = pygame.Vector2(self.location.x + random.uniform(-5 * settings.PIXELS_PER_METER, 5 * settings.PIXELS_PER_METER), self.location.y + random.uniform(-5 * settings.PIXELS_PER_METER, 5 * settings.PIXELS_PER_METER))
            self.direction = pygame.Vector2.normalize(self.targetLocation - self.location)
