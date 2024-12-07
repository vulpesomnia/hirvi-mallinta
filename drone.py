import pygame
import settings, object

directions = [pygame.Vector2(0,1), pygame.Vector2(-1,0), pygame.Vector2(0,1), pygame.Vector2(1,0)]

class Drone(object.GameObject):
    def __init__(self, speed, height, territories, area):
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
        self.area = area

    def fixed_tick(self, dt):
        #collision
        for territory in self.territories:
            if self.direction % 2 == 0:
                distance_y = max(territory.location[1], self.location[1]) - min(territory.location[1], self.location[1])
                distance_x = max(territory.location[0], self.location[0]) - min(territory.location[0], self.location[0])
                if distance_y < territory.radius and (distance_x < territory.radius + self.sight/2):
                    for moose in territory.population:
                        distance_y = max(moose.location[1], self.location[1]) - min(moose.location[1], self.location[1])
                        distance_x = max(moose.location[0], self.location[0]) - min(moose.location[0], self.location[0])
                        if not moose.colliding and (distance_y < 2 and distance_x < self.sight/2 + 2):
                            print(self.mooses, moose.location, self.location)
                            moose.colliding = True
                            self.mooses += 1
                        elif moose.colliding and (distance_y > 2 and distance_x > self.sight/2 + 2):
                            moose.colliding = False
            else:
                distance_y = max(territory.location[1], self.location[1]) - min(territory.location[1], self.location[1])
                distance_x = max(territory.location[0], self.location[0]) - min(territory.location[0], self.location[0])
                if distance_x < territory.radius and (distance_y < territory.radius + self.sight/2):
                    for moose in territory.population:
                        distance_y = max(moose.location[1], self.location[1]) - min(moose.location[1], self.location[1])
                        distance_x = max(moose.location[0], self.location[0]) - min(moose.location[0], self.location[0])
                        if not moose.colliding and (distance_y < self.sight/2 + 2 and distance_x < 2):
                            moose.colliding = True
                            self.mooses += 1
                            print(self.mooses, moose.location, self.location)
                        elif moose.colliding and (distance_y > 2 and distance_x > self.sight/2 + 2):
                            moose.colliding = False

        #movement
        if self.direction % 2 == 0 and ((self.location[1] + self.sight/2) % self.sight < 1 or (self.location[1] + self.sight/2) % self.sight > self.sight-1):
            if self.location[1] > settings.MAP_HEIGHT + self.sight/2:
                settings.is_running = False
            self.location += 2*directions[self.direction]
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(1, self.sight), (255, 0, 255, 50), self.location)
        elif self.direction % 2 == 1 and (self.location[0] > settings.PIXELS_PER_METER * settings.MAP_WIDTH - self.sight/2 or self.location[0] < self.sight/2):
            self.location -= self.velocity
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(self.sight, 1), (255, 0, 255, 50), self.location)
        else:
            self.location += self.velocity * dt
