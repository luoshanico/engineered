import pymunk
import pymunk.pygame_util
import settings.colours
import settings.general
import settings.colours
from builder_objects import Ball

class BuilderPhysics:
    def __init__(self, game):
        self.game = game
        self.setup_space()
        self.add_ground()
        self.add_object_loading_bay()

    def setup_space(self):
        self.game.draw_options = pymunk.pygame_util.DrawOptions(self.game.surface)
        self.game.space = pymunk.Space()
        self.game.space.gravity = 0, 2000

    def add_ground(self):
        segment = pymunk.Segment(
            self.game.space.static_body,
            (0, settings.general.HEIGHT),
            (settings.general.RES),
            20
            )
        segment.elasticity = settings.general.world['elasticity']
        segment.friction = settings.general.world['friction']
        segment.collision_type = settings.general.WORLD_CAT
        self.game.space.add(segment)

    def add_object_loading_bay(self):
        segment = pymunk.Segment(
            self.game.space.static_body,
            (settings.general.loading_bay['width'], settings.general.HEIGHT-20),
            (settings.general.loading_bay['width'],settings.general.HEIGHT-settings.general.loading_bay['height']),
            10
            )
        segment.elasticity = settings.general.world['elasticity']
        segment.friction = settings.general.world['friction']
        segment.collision_type = settings.general.WORLD_CAT
        self.game.space.add(segment)
        self.game.draw_text(self.game.surface, "LOADING BAY", settings.colours.RED, 200, 200)


    def get_events(self,event):
        pass
    
    def update(self):
        # Use a fixed step time or dt from the game if available
        self.game.space.step(1 / self.game.FPS)

    def render(self):
        self.game.space.debug_draw(self.game.draw_options)
