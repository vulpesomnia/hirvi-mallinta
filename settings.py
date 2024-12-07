import math, pygame, camera
def hour_to_time(hour): 
    return hour * 3600 * MAX_FPS 
def time_to_hour(time): 
    time = time / 60 / 3600
    return (math.floor(time), (time-math.floor(time))*60)

def toggle_drone_follow():
    global follow_drone
    follow_drone = not follow_drone
    if follow_drone:
        camera.location = camera.drone.location
    else:
        camera.location = pygame.Vector2(camera.location.x, camera.location.y)

physics_pool = []
render_pool = []

SCREEN_WIDTH = 1280 # 960
SCREEN_HEIGHT = 720 # 540

MAP_HEIGHT = 25000
MAP_WIDTH = 12500

SCREEN_RESIZE_FACTOR = 1 
PIXELS_PER_METER = 1 #Pixels per meter

MAX_FPS = 60
TICK_SPEED = (1 / 60) #Fixed value do not touch!
STARTING_TIME = 9 #In hours like 6 = 6:00 and 15 = 15:00

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

MIN_MOOSE_HEIGHT = 1.7
MAX_MOOSE_HEIGHT = 2.1

MIN_MOOSE_LENGTH = 2.5
MAX_MOOSE_LENGTH = 3

SUNRISE_TIME = 9
SUNSET_TIME = 15

ACTIVE_REST = 0.15
LESS_ACTIVE_REST = 1

MOOSE_DENSITY_PER_THOUSAND_HECTARES = 3.49
MOOSE_AMOUNT = int(MAP_HEIGHT / 1000 * MAP_WIDTH / 1000 * 100 * MOOSE_DENSITY_PER_THOUSAND_HECTARES / 1000)
MOOSE_SPEED = 2

MIN_TERRITORY_RADIUS = 100
MAX_TERRITORY_RADIUS = 500

DRONE_AMOUNT = 1
DRONE_SPEED = 50
DRONE_HOURLY_COST = 100

INVESTMENT_COSTS = 10000 + 2000

SIMULATION_SPEED = 300
SIMULATION_AMOUNT = 1

TOGGLE_RENDERING = True

camera = camera.Camera()
currentSimulation = None
screen = None
rendering_frame = None
scaled_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen_offset = 0
time = hour_to_time(STARTING_TIME)
is_running = True
follow_drone = False

f = open("parameters.txt", "r")
i = 0
for line in f.readlines():
    if line[0] != "#":
        line = line.replace("\n", "")
        num = float(line)
        if i == 0:
            MOOSE_DENSITY_PER_THOUSAND_HECTARES = num
            MOOSE_AMOUNT = int(MAP_HEIGHT / 1000 * MAP_WIDTH / 1000 * 100 * MOOSE_DENSITY_PER_THOUSAND_HECTARES / 1000)
        elif i == 1:
            MOOSE_SPEED = num
        elif i == 2:
            ACTIVE_REST = num
        elif i == 3:
            LESS_ACTIVE_REST = num
        elif i == 4:
            MIN_TERRITORY_RADIUS = num
            MAX_TERRITORY_RADIUS = num+400
        elif i == 5:
            DRONE_AMOUNT = num
        elif i == 6:
            DRONE_SPEED = num
        elif i == 7:
            STARTING_TIME = num
        i += 1



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
