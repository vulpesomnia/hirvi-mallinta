
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
            mooseAmt = random.randint(1, min(3, mooses))
            mooses -= mooseAmt
            success = False
            while not success:
                territoryRadius = random.uniform(territoryMin, territoryMax)
                xOffset = random.uniform(territoryRadius, width-territoryRadius)
                yOffset = random.uniform(territoryRadius, height-territoryRadius)
                position = pygame.Vector2(xOffset, yOffset)
                if len(self.territories) == 0:
                    self.territories.append(territory.Territory(position, territoryRadius * settings.PIXELS_PER_METER, mooseAmt))
                    success = True
                else:
                    for i in range(len(self.territories)):
                        if settings.getSquareDistance(position, self.territories[i].location) < (territoryRadius + self.territories[i].radius)**2:
                            break
                        elif i == len(self.territories)-1:
                            self.territories.append(territory.Territory(position, territoryRadius * settings.PIXELS_PER_METER, mooseAmt))
                            success = True
