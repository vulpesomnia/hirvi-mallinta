import pygame
import settings, object

directions = [pygame.Vector2(0,1), pygame.Vector2(-1,0), pygame.Vector2(0,1), pygame.Vector2(1,0)]

class Drone(object.GameObject):
    def __init__(self, speed, height, territories):
        super().__init__()
        self.sight = 400
        self.location = pygame.Vector2(self.sight/2 + 1, 1)
        self.direction = 2
        self.speed = 50 #m/s
        self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
        self.height = height
        self.mooses = 0
        self.sprite = object.Sprite(pygame.Vector2(self.sight, 1), (255, 0, 255, 50), self.location)
        self.territories = territories

    def fixed_tick(self, dt):
        #collision
        for territory in self.territories:
            if self.direction % 2 == 0:
                distance = max(territory.location[1], self.location[1]) - min(territory.location[1], self.location[1])
                if distance < territory.radius: #and (territory.location[0] - territory.radius > self.location[0] + self.sight/2 or territory.location[0] + territory.radius > self.location[0] - self.sight/2):
                    for moose in territory.population:
                        if not moose.colliding and self.sprite.collisionBox.colliderect(moose.sprite.collisionBox):
                            moose.colliding = True
                            self.mooses += 1
                            print(self.mooses)
            else:
                distance = max(territory.location[1], self.location[1]) - min(territory.location[1], self.location[1])
                if distance < territory.radius: #and (territory.location[1] - territory.radius > self.location[1] + self.sight/2 or territory.location[1] + territory.radius > self.location[1] - self.sight/2):
                    for moose in territory.population:
                        if not moose.colliding and self.sprite.collisionBox.colliderect(moose.sprite.collisionBox):
                            moose.colliding = True
                            self.mooses += 1
                            print(self.mooses)

        #movement
        if self.direction % 2 == 0 and ((self.location[1] + self.sight/2) % self.sight < 1 or (self.location[1] + self.sight/2) % self.sight > self.sight-1):
            self.location += 2*directions[self.direction]
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(self.sight, 1), (255, 0, 255, 50), self.location)
        elif self.direction % 2 == 1 and (self.location[0] > settings.PIXELS_PER_METER * settings.MAP_WIDTH - self.sight/2 or self.location[0] < self.sight/2):
            self.location -= self.velocity
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(1, self.sight), (255, 0, 255, 50), self.location)
        else:
            self.location += self.velocity * dt
