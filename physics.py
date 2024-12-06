import settings

def tick(dt):
    for game_object in settings.physics_pool:
        if callable(getattr(game_object, "fixed_tick", None)):
            game_object.fixed_tick(dt)
