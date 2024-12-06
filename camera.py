import pygame
import settings, object

class Camera(object.GameObject):
    def __init__(self):
        super().__init__()
        self.location = pygame.Vector2(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2)

    def fixed_tick(self, dt):
        self.location = self.location.lerp(self.location, 0.02*dt)
