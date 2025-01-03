import pygame

import settings

class Sprite():
    def __init__(self, size, color, location):
        self.size = size
        self.location = location
        settings.render_pool.append(self)
        self.color = color
        self.rect = pygame.Surface((size.x, size.y))
        if len(color) == 4:
            self.rect.set_alpha(color[3])
        self.rect.fill(color)

class GameObject():
    def __init__(self):
        self.velocity = pygame.math.Vector2()
        self.location = pygame.math.Vector2()
        self.sprite = None
        settings.physics_pool.append(self)
