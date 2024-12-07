import pygame
import settings, object

cameraSpeed = 100
class Camera(object.GameObject):
    def __init__(self):
        super().__init__()
        self.location = pygame.Vector2(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2)
        self.drone = None
        


    def move(self, x, y):
        if settings.follow_drone:
            self.location = self.drone.location
        else:
            self.location += pygame.Vector2(x, y) * cameraSpeed
