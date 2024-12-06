import pygame
import settings, object

directions = [pygame.Vector2(0,1), pygame.Vector2(1,0), pygame.Vector2(0,-1), pygame.Vector2(1,0)]

class Drone(object.GameObject):
    def __init__(self, speed, height):
        super().__init__()
        self.location = pygame.Vector2(-100, 0)
        self.direction = 0
        self.speed = 50 #m/s
        self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
        self.height = height
        self.mooses = 0
        self.sight = 400
        self.sprite = object.Sprite(pygame.Vector2(self.sight, 1), (255, 0, 255, 50), self.location)

    def fixed_tick(self, dt):
        #collision
        #moving
        print(self.velocity)
        if self.location[1] < -settings.SCREEN_HEIGHT/2 or self.location[1] > settings.SCREEN_HEIGHT/2:
            self.location -= 2*directions[self.direction]
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(self.sight, 1), (255, 0, 255, 50), self.location)
        elif self.location[0] % self.sight < 1 and self.location[0] % self.sight > -1:
            self.location += 2*directions[self.direction]
            self.direction += 1
            self.direction %= 4
            self.velocity = directions[self.direction] * self.speed * settings.PIXELS_PER_METER * settings.TICK_SPEED
            self.sprite = object.Sprite(pygame.Vector2(1, self.sight), (255, 0, 255, 50), self.location)
        else:
            self.location += self.velocity * dt
