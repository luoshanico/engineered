import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
from settings import general_settings
from settings.menu_settings import menu_map

class Constraints:
    def __init__(self, game, obj1, obj2):
        self.game = game
        self.get_constrained_objects(obj1, obj2)
        self.get_attributes()
        self.get_anchors()
        self.create_body()
        self.create_sensor_shape()
        self.add_labels()
        self.add_body_to_space()
        self.add_shape_to_space()
        self.add_constraint_to_manager()

    def get_constrained_objects(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def get_anchors(self):
        self.anchor1 = self.obj1.selected_anchor
        self.anchor2 = self.obj2.selected_anchor

    def create_sensor_shape(self):
        anchor2_rel_obj1 = self.get_anchor2_rel_obj1()
        self.sensor_shape = pymunk.Segment(self.obj1.body, self.anchor1, anchor2_rel_obj1, 10)
        self.sensor_shape.sensor = True
    
    def get_anchor2_rel_obj1(self):       
        anchor2_world = self.obj2.body.local_to_world(self.anchor2)
        return self.obj1.body.world_to_local(anchor2_world)

    def delete_sensor_shape(self):
        self.game.space.remove(self.sensor_shape)

    def add_body_to_space(self):
        self.game.space.add(self.body)

    def add_shape_to_space(self):
        self.game.space.add(self.sensor_shape)

    def add_constraint_to_manager(self):
        self.game.state_stack[-1].manager.store_constraint(
            self,
            self.obj1,
            self.obj2,
            self.anchor1,
            self.anchor2
        )
    
    def apply_updated_attributes(self):
        self.delete()
        self.get_attributes()
        self.create_body()
        self.create_sensor_shape()
        self.add_labels()
        self.add_body_to_space()
        self.add_shape_to_space()

    def refresh_constraint_after_updated_object(self):
        self.delete()
        self.create_body()
        self.create_sensor_shape()
        self.add_labels()
        self.add_body_to_space()
        self.add_shape_to_space()

    def delete(self):
        self.game.space.remove(self.body, self.sensor_shape)

       
    def render(self, surface):
        self.delete_sensor_shape()
        self.create_sensor_shape()
        self.add_labels()
        self.add_shape_to_space()

    def update(self):
        pass
    
    def apply_selected_color(self):
        pass

    def apply_deselected_color(self):
        pass

    def add_anchor_selection(self,p):
        pass



class DampedSpring(Constraints):
    def get_attributes(self):
        self.attributes = tuple([float(inputs['input_field'].value) for inputs in menu_map['damped_spring']['inputs']])
        self.rest_length, self.stiffness, self.damping = self.attributes
    
    def create_body(self):
        self.body = pymunk.DampedSpring(
            self.obj1.body,
            self.obj2.body,
            self.anchor1,
            self.anchor2,
            self.rest_length, 
            self.stiffness, 
            self.damping)
        
    def add_labels(self):
        self.component_type = 'constraint'
        self.component_subtype = 'damped_spring'
        self.sensor_shape.owner = self

    