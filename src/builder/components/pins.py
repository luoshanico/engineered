import pymunk.pygame_util
from pygame.locals import *

class Pins:
    def __init__(self, game, obj, pivot_point):
        self.game = game
        self.obj = obj
        self.pivot_point = pivot_point
        self.get_attributes()
        self.create_body()
        self.add_labels()
        self.add_body_to_space()
        self.add_pin_to_manager()
    
    def get_attributes(self):
        self.pivot_point = self.pivot_point
    
    def create_body(self):
        self.body = pymunk.PivotJoint(
            self.obj.body,
            self.game.space.static_body,
            self.pivot_point)

    def add_labels(self):
        self.component_type = 'pin'
        self.component_subtype = 'pin'

    def delete_shape(self):
        self.game.space.remove(self.shape)

    def add_body_to_space(self):
        self.game.space.add(self.body)

    def add_pin_to_manager(self):
        self.game.state_stack[-1].manager.store_pin(
            self,
            self.obj,
            self.pivot_point
        )
    
    def apply_updated_attributes(self):
        self.delete()
        self.get_attributes()
        self.create_body()
        self.add_labels()
        self.add_body_to_space()

    def refresh_pin_after_updated_object(self):
        self.delete()
        self.create_body()
        self.add_labels()
        self.add_body_to_space()

    def delete(self):
        self.game.space.remove(self.body)
       
    def render(self, surface):
        pass

    def update(self):
        pass
    
    def apply_selected_color(self):
        pass

    def apply_deselected_color(self):
        pass

    def add_anchor_selection(self,p):
        pass