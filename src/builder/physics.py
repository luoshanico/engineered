import pymunk
import pymunk.pygame_util
import settings.general_settings
from builder.objects import Ball

class BuilderPhysics:
    def __init__(self, game):
        self.game = game
        self.setup_space()
        self.add_ground()
        self.add_bay1()
        self.add_bay2()

    def setup_space(self):
        self.game.draw_options = pymunk.pygame_util.DrawOptions(self.game.surface)
        self.game.space = pymunk.Space()
        self.game.space.gravity = 0, 2000

    def add_ground(self):
        segment = pymunk.Segment(
            self.game.space.static_body,
            (0, settings.general_settings.HEIGHT),
            (settings.general_settings.RES),
            20
            )
        segment.elasticity = settings.general_settings.world['elasticity']
        segment.friction = settings.general_settings.world['friction']
        segment.collision_type = settings.general_settings.WORLD_CAT
        self.game.space.add(segment)

    def add_bay1(self):
        segment = pymunk.Segment(
            self.game.space.static_body,
            (settings.general_settings.bay1['width'], settings.general_settings.HEIGHT-20),
            (settings.general_settings.bay1['width'],settings.general_settings.HEIGHT-settings.general_settings.bay1['height']),
            10
            )
        segment.elasticity = settings.general_settings.world['elasticity']
        segment.friction = settings.general_settings.world['friction']
        segment.collision_type = settings.general_settings.WORLD_CAT
        self.game.space.add(segment)
        self.game.draw_text(self.game.surface, "LOADING BAY", settings.general_settings.RED, 200, 200)

    def add_bay2(self):
        segment = pymunk.Segment(
            self.game.space.static_body,
            (settings.general_settings.bay2['width'], settings.general_settings.HEIGHT-20),
            (settings.general_settings.bay2['width'],settings.general_settings.HEIGHT-settings.general_settings.bay2['height']),
            10
            )
        segment.elasticity = settings.general_settings.world['elasticity']
        segment.friction = settings.general_settings.world['friction']
        segment.collision_type = settings.general_settings.WORLD_CAT
        self.game.space.add(segment)
        self.game.draw_text(self.game.surface, "LOADING BAY", settings.general_settings.RED, 200, 200)


    def get_events(self,event):
        pass
    
    def update(self):
        # Use a fixed step time or dt from the game if available
        self.game.space.step(1 / self.game.FPS)

    def render(self):
        self.game.space.debug_draw(self.game.draw_options)
