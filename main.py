import pygame, random
import settings, physics, rendering, events, drone, map, simulation
from pygame.locals import *

pygame.init()
# - - - - - -#
if settings.TOGGLE_RENDERING:
    pygame.display.set_caption("Hirvimallinnusohjelma")
    settings.screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT), pygame.RESIZABLE)
    settings.rendering_frame = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
game_clock = pygame.time.Clock()

previous_frametime = pygame.time.get_ticks() 
accumulated_frametime = 0

forestMap = None
settings.currentSimulation = simulation.Simulation(1)
simulations = []

def reset_simulation():
    global forestMap
    settings.is_running = True
    settings.physics_pool = []
    settings.render_pool = []
    forestMap = map.Map(settings.MAP_WIDTH * settings.PIXELS_PER_METER, settings.MAP_HEIGHT * settings.PIXELS_PER_METER, settings.MOOSE_AMOUNT)

events.setup_events()
for _ in range(settings.SIMULATION_AMOUNT):
    reset_simulation()
    mainDrone = drone.Drone(50, 221 * settings.PIXELS_PER_METER, forestMap.territories, 1)
    settings.camera.drone = mainDrone
    while True:
    # - Main Physics - #§
        current_frametime = pygame.time.get_ticks()
    #Adds the time the previous frame took to the accumulator
        accumulated_frametime += (current_frametime - previous_frametime) / 1000.0
    #Prepare for next frame by setting previous frametime's timestamp
        previous_frametime = current_frametime
        events.event_listener()
        while accumulated_frametime > settings.TICK_SPEED:
            physics.tick(settings.SIMULATION_SPEED)
            accumulated_frametime -= settings.TICK_SPEED
        if accumulated_frametime > 0:
            physics.tick(accumulated_frametime *settings.SIMULATION_SPEED / settings.TICK_SPEED)
            accumulated_frametime = 0

    #Possibly move camera position update to sync with physics update.
        if settings.TOGGLE_RENDERING:
            settings.rendering_frame = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
            settings.screen.fill(settings.BLACK)
            settings.rendering_frame.fill(settings.WHITE)
            rendering.render_all(settings.camera.location) 

    # - - - - - - - - - -#
            scaled_rendering_frame = pygame.transform.scale(settings.rendering_frame, settings.scaled_size)

            settings.screen.blit(scaled_rendering_frame, (settings.screen_offset, 0))
            pygame.display.flip()
            game_clock.tick(settings.MAX_FPS)
        if not settings.is_running:
            break

    simulations.append(settings.currentSimulation)
    settings.currentSimulation = simulation.Simulation(settings.currentSimulation.id+1)
data = []
name = "output-raw-" + str(random.randint(1, 300000)) + ".txt"
f = open("./output/" + name, "a")
f.write("FORMAT:" + " ")
f.write("AIKA" + " ")
f.write("HINTA" + " ")
f.write("HIRVIÄ LÖYTYNYT" + " ")
f.write("VIRHE" + " ")
f.write("SUHTEELLINEN VIRHE" + "\n")

for s in simulations:
    data.append(s.show_results())
    f.write(str(data[len(data)-1][0]) + " ")
    f.write(str(data[len(data)-1][1]) + " ")
    f.write(str(data[len(data)-1][2]) + " ")
    f.write(str(data[len(data)-1][3]) + " ")
    f.write(str(data[len(data)-1][3]/settings.MOOSE_AMOUNT) + "\n")

    # return (self.time, self.cost, self.mooseFound, virhe)
f.write("# - YHTEENVETO - #" + "\n")
virhe_keskiarvo = 0
for d in data:
    virhe_keskiarvo += d[3]
f.write("VIRHE KESKIARVO: " + str(virhe_keskiarvo/len(data)) + "\n")
f.close()
