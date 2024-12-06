import pygame, settings

class Sprite():
    def __init__(self, size, color, location):
        self.size = pygame.Vector2(size.x, size.y)
        self.location = location
        settings.render_pool.append(self)
        self.color = color
        self.rect = pygame.Surface((size.x, size.y))
        self.rect.fill(color)

class GameObject():
    def __init__(self):
        self.velocity = pygame.math.Vector2()
        self.location = pygame.math.Vector2()
        self.sprite = None
        settings.physics_pool.append(self)
