import pygame, random
import settings, object, moose

class Territory(object.GameObject):
    def __init__(self, location, radius, mooseNumber):
        super().__init__()
        self.location = location
        self.radius = radius
        self.population = []
        self.restTime = 0
        randDir = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))) * random.uniform(0, radius)
        for n in range(mooseNumber):
            xOffset = pygame.Vector2(n*5*settings.PIXELS_PER_METER, 0)
            if n > 0:
                self.population.append(moose.Moose(self.population[0].location - xOffset, random.uniform(settings.MIN_MOOSE_HEIGHT, settings.MAX_MOOSE_HEIGHT), random.uniform(settings.MIN_MOOSE_LENGTH, settings.MAX_MOOSE_LENGTH) * settings.PIXELS_PER_METER, self, self.population[n-1], 100))
            else:
                self.population.append(moose.Moose(self.location + randDir , random.uniform(1.7, 2.1), random.uniform(2.5, 3) * settings.PIXELS_PER_METER, self, 100))
        self.sprite = object.Sprite(pygame.Vector2(radius*2, radius*2), (0, 255, 126, 50), self.location)
        pygame.draw.circle(self.sprite.rect, (255, 255, 255), (radius, radius), radius)

    def rest(self, time):
        self.restTime = settings.hour_to_time(time)
        for muusi in self.population:
            muusi.resting = True

    def fixed_tick(self, dt):
        if self.restTime > 0:
            self.restTime = self.restTime-dt
        elif self.restTime < 0:
            self.restTime = 0
            for muusi in self.population:
                muusi.resting = False
        else:
            if settings.time > settings.hour_to_time(settings.SUNRISE_TIME) and settings.time < settings.hour_to_time(settings.SUNSET_TIME):
                if settings.time == settings.hour_to_time(settings.SUNRISE_TIME+1):
                    self.rest(settings.ACTIVE_REST)
                elif settings.time == settings.hour_to_time((settings.SUNRISE_TIME+settings.SUNSET_TIME)/2):
                    self.rest(settings.ACTIVE_REST)
                elif settings.time == settings.hour_to_time(settings.SUNSET_TIME):
                    self.rest(settings.ACTIVE_REST)
            else:
                if settings.time % settings.hour_to_time(2) == 0:
                    self.rest(settings.LESS_ACTIVE_REST)
