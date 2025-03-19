import pymunk.pygame_util
from pygame.locals import *

class Constraints:
    def __init__(self, game, obj1, obj2):
        self.game = game
        self.get_constrained_objects(obj1, obj2)
        self.get_anchors()
        self.get_attributes()
        self.create_body()
        self.create_shape()
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

    def create_shape(self):
        anchor2_rel_obj1 = self.get_anchor2_rel_obj1()
        self.shape = pymunk.Segment(self.obj1.body, self.anchor1, anchor2_rel_obj1, 10)
        self.shape.sensor = True
    
    def get_anchor2_rel_obj1(self):       
        anchor2_world = self.obj2.body.local_to_world(self.anchor2)
        return self.obj1.body.world_to_local(anchor2_world)

    def delete_shape(self):
        self.game.space.remove(self.shape)

    def add_body_to_space(self):
        self.game.space.add(self.body)

    def add_shape_to_space(self):
        self.game.space.add(self.shape)

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
        self.create_shape()
        self.add_labels()
        self.add_body_to_space()
        self.add_shape_to_space()

    def refresh_constraint_after_updated_object(self):
        self.delete()
        self.create_body()
        self.create_shape()
        self.add_labels()
        self.add_body_to_space()
        self.add_shape_to_space()

    def delete(self):
        self.game.space.remove(self.body, self.shape)

       
    def render(self, surface):
        self.delete_shape()
        self.create_shape()
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
        self.get_input_fields()
        self.attributes = tuple([float(input_field.value) for input_field in self.input_fields])
        self.rest_length, self.stiffness, self.damping = self.attributes

    def get_input_fields(self):
        menu_section = self.game.state_stack[-1].menu.menu_map['damped_spring']['items']
        self.input_fields = [item['object'] for item in menu_section if item['type']=='input']
    
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
        self.shape.owner = self


class PinJoint(Constraints):
    def get_attributes(self):
        pass

    def create_body(self):
        self.body = pymunk.PinJoint(
            self.obj1.body,
            self.obj2.body,
            self.anchor1,
            self.anchor2)

    def add_labels(self):
        self.component_type = 'constraint'
        self.component_subtype = 'pin_joint'
        self.shape.owner = self


class PivotJoint(Constraints):
    def get_attributes(self):
        anchor_1_world = self.obj1.body.local_to_world(self.anchor1)
        anchor_2_world = self.obj2.body.local_to_world(self.anchor2)
        self.pivot_point = (anchor_2_world + anchor_1_world) // 2 

    def create_body(self):
        self.body = pymunk.PivotJoint(
            self.obj1.body,
            self.obj2.body,
            self.pivot_point)

    def add_labels(self):
        self.component_type = 'constraint'
        self.component_subtype = 'pivot_joint'
        self.shape.owner = self
    