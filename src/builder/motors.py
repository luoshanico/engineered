import pymunk.pygame_util
from pygame.locals import *
from settings.menu_map import menu_map
from math import pi


class Motor:
    def __init__(self, game, driven_object):
        self.game = game
        self.driven_object = driven_object
        self.get_attributes()
        self.add_labels()
        self.create_body()
        self.add_body_to_space()
        self.add_motor_to_manager()
        
    def get_attributes(self):
        self.get_input_fields()
        self.attributes = tuple([float(input_field.value) for input_field in self.input_fields])
        self.rpm = self.attributes[0]
        self.angular_velocity = self.rpm * (2 * pi) / 60
        self.max_force = self.attributes[1] * 1000

    def get_input_fields(self):
        menu_section = self.game.state_stack[-1].menu.menu_map['motor']['items']
        self.input_fields = [item['object'] for item in menu_section if item['type']=='input']
    
    def add_labels(self):
        self.component_type = 'motor'
        self.component_subtype = 'motor'

    def create_body(self):
        self.body = pymunk.SimpleMotor(self.game.space.static_body,
                                        self.driven_object.body,
                                        self.angular_velocity)
        self.body.max_force = self.max_force
        
    def add_body_to_space(self):
        self.game.space.add(self.body)
    
    def update(self):
        pass

    def render(self, surface):
        pass

    def delete(self):
        self.game.space.remove(self.body)

    def add_motor_to_manager(self):
        self.game.state_stack[-1].manager.store_motor(
            self,
            self.driven_object,
        )

    def refresh_motor_after_updated_object(self):
        self.delete()
        self.create_body()
        self.add_labels()
        self.add_body_to_space()