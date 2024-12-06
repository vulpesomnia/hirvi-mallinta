
import pygame, random
import settings, object, moose, territory

territoryMin = 200
territoryMax = 2000

class Map():
    def __init__(self, height, width, mooses):
        # Create territories around and create lake
        self.height = height
        self.width = width
        self.territories = []
        self.sprite = object.Sprite(pygame.Vector2(width, height), (0, 255, 126), pygame.Vector2(width/2, height/2)) 
        while mooses > 0:
            mooseAmt = random.randint(1, min(10, mooses))
            mooses -= mooseAmt
            territoryRadius = random.uniform(territoryMin, territoryMax)
            xOffset = random.uniform(territoryRadius, width-territoryRadius)
            yOffset = random.uniform(territoryRadius, height-territoryRadius)
            self.territories.append(territory.Territory(pygame.Vector2(xOffset, yOffset), territoryRadius * settings.PIXELS_PER_METER, mooseAmt))
