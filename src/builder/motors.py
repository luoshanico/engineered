import pymunk.pygame_util
from pygame.locals import *
from settings.menu_settings import menu_map
from math import pi


class Motor:
    def __init__(self, game, driven_object):
        self.game = game
        self.driven_object = driven_object
        self.get_attributes()
        self.get_labels()
        self.create_motor()
    
    def get_attributes(self):
        self.attributes = tuple([float(inputs['input_field'].value) for inputs in menu_map['motor']['inputs']])
        self.rpm = self.attributes[0]
        self.angular_velocity = self.rpm * (2 * pi) / 60
        self.max_force = self.attributes[1] * 1000

    
    def get_labels(self):
        self.component_type = 'motor'
        self.component_subtype = 'motor'

    def create_motor(self):
        self.motor = pymunk.SimpleMotor(self.game.space.static_body,
                                        self.driven_object.body,
                                        self.angular_velocity)
        self.motor.max_force = self.max_force
        self.game.space.add(self.motor)
    
    def update(self):
        pass

    def render(self, surface):
        pass

    def remove(self):
        self.game.space.remove(self.motor)