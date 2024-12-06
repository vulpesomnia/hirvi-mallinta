
import pygame, settings

from pygame.locals import * 

ACTIVE_EVENTS = {}

def setup_events():
    global ACTIVE_EVENTS
    ACTIVE_EVENTS = {
            (pygame.QUIT, 0) : "pygame.quit()",
            (pygame.VIDEORESIZE, 0) : "settings.screen_resize(event.h, event.w)",
            }

def event_listener():
    event_keys = ACTIVE_EVENTS.keys()
    #Listener for general events.
    for event in pygame.event.get():
        key = (event.type, 0)
        if key in event_keys:
            eval(ACTIVE_EVENTS[key])

    keys = pygame.key.get_pressed()
    #Listener for key presses
    for key in event_keys:
        if keys[key[0]]:
            eval(ACTIVE_EVENTS[key])
