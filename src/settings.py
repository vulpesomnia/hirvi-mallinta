import pygame
import math

import camera

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


# Constants and parameters
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MAP_HEIGHT = 25000
MAP_WIDTH = 12500

PIXELS_PER_METER = 1 

MAX_FPS = 60
TICK_SPEED = (1 / 60) # NOTE: Fixed value do not touch!
STARTING_TIME = 9 # NOTE: In hours like 6 = 6:00 and 15 = 15:00

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

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

DRONE_SPEED = 50
DRONE_HOURLY_COST = 100

INVESTMENT_COSTS = 10000 + 2000

SIMULATION_SPEED = 10
SIMULATION_AMOUNT = 10

TOGGLE_RENDERING = True

# Global variables
physics_pool = []
render_pool = []

camera = camera.Camera()

screen = None
rendering_frame = None
scaled_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen_offset = 0

time = hour_to_time(STARTING_TIME)
currentSimulation = None

is_running = True
follow_drone = False

# Reading the parameters
f = open("../parameters.txt", "r")
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
            DRONE_SPEED = num
        elif i == 6:
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

def get_square_distance(pos1, pos2):
    return (pos1.x-pos2.x)**2 + (pos1.y-pos2.y)**2
