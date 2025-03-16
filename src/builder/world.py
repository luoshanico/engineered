import pymunk
import pymunk.pygame_util
import settings.general_settings

class BuilderWorld:
    def __init__(self, game):
        self.game = game
        self.get_settings()
        self.add_box()    

    def get_settings(self):
        self.elasticity = 0.8
        self.friction = 0.2
        self.width, self.height = settings.general_settings.RES

    def add_box(self):
        self.box_thickness = 5
        self.box_dims = [
            ((0, self.height),(self.width, self.height)),  # floor
            ((0, 0),(self.width, 0)),  # ceiling
            ((self.width, 0),(self.width, self.height)),  # right wall
            ((0, 0),(0, self.height)),  # left wall
            ]
        for dims in self.box_dims:
            self.add_box_side(dims)

    def add_box_side(self,dims):
        segment = pymunk.Segment(
            self.game.space.static_body,
            *dims,
            self.box_thickness
            )
        segment.elasticity = self.elasticity
        segment.friction = self.friction
        segment.collision_type = settings.general_settings.WORLD_CAT
        self.game.space.add(segment)

    def get_events(self,event):
        pass
    
    def update(self):
        pass

    def render(self):
        pass