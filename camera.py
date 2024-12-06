import pygame
import settings, object

cameraSpeed = 100
class Camera(object.GameObject):
    def __init__(self):
        super().__init__()
        self.location = pygame.Vector2(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2)

    def move(self, x, y):
        self.location += pygame.Vector2(x, y) * cameraSpeed
