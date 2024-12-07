import math, pygame, camera

physics_pool = []
render_pool = []

SCREEN_WIDTH = 1280 # 960
SCREEN_HEIGHT = 720 # 540

MAP_WIDTH = 25000
MAP_HEIGHT = 12500

SCREEN_RESIZE_FACTOR = 1 
PIXELS_PER_METER = 1 #Pixels per meter

MAX_FPS = 60
TICK_SPEED = (1 / 60) #Fixed value do not touch!

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

MIN_MOOSE_HEIGHT = 1.7
MAX_MOOSE_HEIGHT = 2.1

MIN_MOOSE_LENGTH = 2.5
MAX_MOOSE_LENGTH = 3

MOOSE_DENSITY_PER_THOUSAND_HECTARES = 3.49
MOOSE_AMOUNT = int(MAP_HEIGHT / 1000 * MAP_WIDTH / 1000 * 100 * MOOSE_DENSITY_PER_THOUSAND_HECTARES / 1000)

MIN_TERRITORY_RADIUS = 100
MAX_TERRITORY_RADIUS = 500

camera = camera.Camera()
screen = None
rendering_frame = None
scaled_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen_offset = 0

def screen_resize(event_height, event_width):
    global scaled_size, screen_offset, screen
    aspect_ratio = 16/9
    new_height = event_height
    new_width = math.ceil(new_height * aspect_ratio)
    if (new_height < SCREEN_HEIGHT) or (event_width < SCREEN_WIDTH):
        new_width, new_height = SCREEN_WIDTH, SCREEN_HEIGHT 
        screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
        screen_offset = 0
    else:
        screen_offset = (event_width - new_width) // 2
    scaled_size = (new_width, new_height)

def screen_to_world(screen_location):
    return screen_location / SCREEN_RESIZE_FACTOR

def world_to_screen(world_location):
    return pygame.math.Vector2(round(world_location[0] * SCREEN_RESIZE_FACTOR), round(world_location[1] * SCREEN_RESIZE_FACTOR))

def getSquareDistance(pos1, pos2):
    return (pos1.x-pos2.x)**2 + (pos1.y-pos2.y)**2
