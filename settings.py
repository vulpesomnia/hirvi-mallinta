import math, pygame

physics_pool = []
render_pool = []

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

SCREEN_RESIZE_FACTOR = 1 
PIXELS_PER_METER = 2 #Pixels per meter

MAX_FPS = 60

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

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


