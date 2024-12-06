import pygame
import settings, object

class Camera(object.GameObject):
    def __init__(self):
        super().__init__()
        self.location = pygame.Vector2(0, 0)

    def fixed_tick(self, dt):
        self.location = self.location.lerp(settings.world_to_screen((0,0)), 0.02*dt)
