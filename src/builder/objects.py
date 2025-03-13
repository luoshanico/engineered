import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
import colorsys

from settings import general_settings
from settings.menu_settings import menu_map
from builder.object_controls import ObjectControls
from builder.object_manager import ObjectManager

class Objects:
    def __init__(self,game):
        self.game = game
        self.controls = ObjectControls(game)
        self.manager = ObjectManager(game)
    
    def get_initial_position(self):
        self.body.position = (general_settings.loading_bay['width'] // 2, 250)
    
    def add_to_space(self):
        self.game.space.add(self.body, self.shape)
        # self.game.ball_body = self.body
        # self.game.ball_shape = self.shape

    def apply_updated_attributes(self, game):
        self.store_current_position()
        self.delete()
        self.get_attributes()
        self.create_body()
        self.create_shape()
        self.add_labels()
        self.restore_position()
        self.add_to_space()

    def delete(self):
        self.game.space.remove(self.body, self.shape)
    
    def store_current_position(self):
        pos = self.body.position
        self.current_position = (int(pos.x), int(pos.y))

    def restore_position(self):
        self.body.position = self.current_position

    def apply_color_to_indicate_selected(self):
        self.normal_rgb = self.color
        self.color = self.fade_color(self.color)

    def apply_deselected_color(self):
        self.color = self.normal_rgb

    def fade_color(self, rgb, fade_factor=0.5):
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        s *= fade_factor
        r_new, g_new, b_new = colorsys.hls_to_rgb(h, l, s)
        return (int(r_new * 255), int(g_new * 255), int(b_new * 255))

    
    def update(self):
        pass
    
            


class Ball(Objects):
    def __init__(self,game):
        self.game = game
        self.get_attributes()
        self.create_body()
        self.create_shape()
        self.add_labels()
        self.get_initial_position()
        self.get_initial_color()
        self.add_to_space()
           
    def get_attributes(self):
        print([inputs['input_field'].value for inputs in menu_map['ball']['inputs']])
        self.attributes = tuple([float(inputs['input_field'].value) for inputs in menu_map['ball']['inputs']])
        self.mass, self.radius, self.elasticity, self.friction = self.attributes

    def create_body(self):
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)

    def create_shape(self):
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction
        self.shape.collision_type = general_settings.OBJECT_CAT
    
    def add_labels(self):
        self.object_type = 'ball'
        self.shape.owner = self  # Now when we hit shape with mouse we can identify the underlying object

    def get_initial_color(self):
        self.color = general_settings.BLUE
    
    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))

    
class DampedSpring(Objects):
    def __init__(self, game, obj1, obj2):
        self.game = game
        self.get_attributes()
        self.create_body(obj1, obj2)
        self.add_labels()
        self.add_to_space()
           
    def get_attributes(self):
        self.attributes = tuple([float(inputs['input_field'].value) for inputs in menu_map['damped_spring']['inputs']])
        self.rest_length, self.stiffness, self.damping = self.attributes

    def create_body(self, obj1, obj2):
        self.body = pymunk.DampedSpring(
            obj1.body,
            obj2.body,
            (60, 0),
            (-60, 0),
            self.rest_length, 
            self.stiffness, 
            self.damping)
    
    def add_labels(self):
        self.object_type = 'damped_spring'
        self.owner = self

    def add_to_space(self):
        self.game.space.add(self.body)
    
    def render(self, surface):
        pass
    


        
        


class Rectangle:
    def __init__(self, game):
        self.pos = (general_settings.loading_bay['width'] // 2, 250)
        self.size = self.width, self.height = 20,60
        self.mass = 1
        self.moment = pymunk.moment_for_box(self.mass, self.size)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = self.pos
        self.body.angle = 0
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        self.color = general_settings.RED
        self.shape.collision_type = general_settings.OBJECT_CAT
        game.space.add(self.body, self.shape)

    def render(self, surface):
        vertices = self.shape.get_vertices()
        vertices = [v.rotated(self.body.angle) + self.body.position for v in vertices]
        points = [(int(v.x), int(v.y)) for v in vertices]
        pg.draw.polygon(surface, self.color, points)
