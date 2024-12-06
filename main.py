import pygame
import settings, physics, rendering, camera, object, events, moose
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Hirvimallinnusohjelma")
# - - - - - -#
settings.screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT), pygame.RESIZABLE)
settings.rendering_frame = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
game_clock = pygame.time.Clock()


camera = camera.Camera()

previous_frametime = pygame.time.get_ticks() 
accumulated_frametime = 0


test = moose.Moose(pygame.Vector2(0, 0), 10, 1.8 * settings.PIXELS_PER_METER, "a")

events.setup_events()
while True:
    # - Main Physics - #
    
    current_frametime = pygame.time.get_ticks()
    #Adds the time the previous frame took to the accumulator
    accumulated_frametime += (current_frametime - previous_frametime) / 1000.0
    #Prepare for next frame by setting previous frametime's timestamp
    previous_frametime = current_frametime
    events.event_listener()
    while accumulated_frametime > settings.TICK_SPEED:
        physics.tick(1)
        accumulated_frametime -=  settings.TICK_SPEED
    if accumulated_frametime > 0:
        physics.tick(accumulated_frametime /  settings.TICK_SPEED)
        accumulated_frametime = 0

    #Possibly move camera position update to sync with physics update.
    settings.rendering_frame = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    settings.screen.fill(settings.BLACK)
    settings.rendering_frame.fill(settings.WHITE)
    rendering.render_all(camera.location) 

    # - - - - - - - - - -#
    scaled_rendering_frame = pygame.transform.scale(settings.rendering_frame, settings.scaled_size)

    settings.screen.blit(scaled_rendering_frame, (settings.screen_offset, 0))
    pygame.display.flip()
    game_clock.tick(settings.MAX_FPS)