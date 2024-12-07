import settings

def tick(dt):
    for game_object in settings.physics_pool:
        if callable(getattr(game_object, "fixed_tick", None)):
            game_object.fixed_tick(dt)
    settings.time += dt
    settings.currentSimulation.time += dt
    #clock = settings.time_to_hour(settings.time)
    #print(str(clock[0]) + "h " + str(clock[1]) + "m")
    if settings.time >= settings.hour_to_time(24):
        settings.time = 0
