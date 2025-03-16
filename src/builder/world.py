import pymunk
import pymunk.pygame_util
import settings.general_settings

class BuilderWorld:
    def __init__(self, game):
        self.game = game
        self.add_ground()
        self.add_bay1()
        self.add_bay2()       

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
        pass

    def render(self):
        pass