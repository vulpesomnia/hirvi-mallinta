import pygame

import settings
import object

cameraSpeed = 100
class Camera(object.GameObject):
    def __init__(self):
        super().__init__()
        self.location = pygame.Vector2(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2)
        self.drone = None

    def move(self, x, y):
        if not settings.follow_drone:
           self.location += pygame.Vector2(x, y) * cameraSpeed
