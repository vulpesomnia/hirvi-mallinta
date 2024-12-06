import settings

SCREEN_CENTERING = (settings.SCREEN_WIDTH//2, settings.SCREEN_HEIGHT//2)
def render_all(camera_pos):
    for sprite in settings.render_pool:
        render_location = settings.world_to_screen(sprite.location) - camera_pos + SCREEN_CENTERING 
        settings.rendering_frame.blit(sprite.rect, render_location)
