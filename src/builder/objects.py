import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
import colorsys
import math

from settings import general_settings
from settings.menu_settings import menu_map

class Objects:
    def __init__(self,game):
        self.game = game
        self.get_attributes()
        self.create_body()
        self.create_shape()
        self.add_labels()
        self.get_initial_position()
        self.get_initial_color()
        self.selected_anchor = None
        self.add_to_space()
    
    def get_initial_position(self):
        self.body.position = (150, 250)
    
    def add_to_space(self):
        self.game.space.add(self.body, self.shape)

    def apply_updated_attributes(self):
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

    def apply_selected_color(self):
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
    
    def add_anchor_selection(self,p):
        local_p = self.body.world_to_local(p)
        self.selected_anchor = self.snap_to_anchor_points(local_p)
        print(f"{self.selected_anchor}")
        
    def snap_to_anchor_points(self, p):
        snap_horizon = general_settings.snap_horizon
        snap_points = self.anchor_snap_points()
        print(f"{snap_points=}")
        closest = min(snap_points, key=lambda pt: self.distance(p,pt))
        return p if self.distance(closest,p) > snap_horizon else closest

    def distance(self, p1, p2):
        return math.hypot(p1[0]-p2[0], p1[1] - p2[1])

    def clear_anchor_selection(self):
        self.selected_anchor = None

    def draw_anchor_marker(self, surface):
        if self.selected_anchor:
            world_anchor = self.body.local_to_world(self.selected_anchor)
            pg.draw.circle(surface, general_settings.RED, (int(world_anchor.x),int(world_anchor.y)), 2)

    def update(self):
        pass
    
            


class Ball(Objects):          
    def get_attributes(self):
        self.get_input_fields()
        self.attributes = tuple([float(input_field.value) for input_field in self.input_fields])
        self.mass, self.radius, self.elasticity, self.friction = self.attributes

    def get_input_fields(self):
        menu_section = self.game.state_stack[-1].menu.menu_map['ball']['items']
        self.input_fields = [item['object'] for item in menu_section if item['type']=='input']

    def create_body(self):
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)

    def create_shape(self):
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction
        self.shape.collision_type = general_settings.OBJECT_CAT
    
    def add_labels(self):
        self.component_type = 'object'
        self.component_subtype = 'ball'
        self.shape.owner = self  # Now when we hit shape with mouse we can identify the underlying object

    def get_initial_color(self):
        self.color = general_settings.GREEN
    
    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))
        self.draw_anchor_marker(surface)

    def anchor_snap_points(self):
        return [(0,0)]
    

class Bar(Objects):          
    def get_attributes(self):
        self.get_input_fields()
        self.attributes = tuple([float(input_field.value) for input_field in self.input_fields])
        self.mass, self.length, self.elasticity, self.friction = self.attributes

    def get_input_fields(self):
        menu_section = self.game.state_stack[-1].menu.menu_map['bar']['items']
        self.input_fields = [item['object'] for item in menu_section if item['type']=='input']
    
    def create_body(self):
        self.thickness = 10
        self.size = self.length, self.thickness
        self.moment = pymunk.moment_for_box(self.mass, self.size)
        self.body = pymunk.Body(self.mass, self.moment)

    def create_shape(self):
        self.shape = pymunk.Segment(self.body, (0, self.length//2), (0, -self.length//2), self.thickness//2)
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction
        self.shape.collision_type = general_settings.OBJECT_CAT
    
    def add_labels(self):
        self.component_type = 'object'
        self.component_subtype = 'bar'
        self.shape.owner = self  # Now when we hit shape with mouse we can identify the underlying object

    def get_initial_color(self):
        self.color = general_settings.BLUE
    
    def render(self, surface):
        vertices = self.segment_to_poly()
        # vertices = [v.rotated(self.body.angle) + self.body.position for v in vertices]
        points = [(int(v.x), int(v.y)) for v in vertices]
        pg.draw.polygon(surface, self.color, points)
        self.draw_anchor_marker(surface)

    def anchor_snap_points(self):
        return [(0,0), *self.end_points()]
    
    def segment_to_poly(self):
        # Get endpoints in world coordinates.
        A = self.shape.body.local_to_world(self.shape.a)
        B = self.shape.body.local_to_world(self.shape.b)
        r = self.shape.radius
        
        # Compute the normalized vector from A to B.
        v = (B - A).normalized()
        # Get a perpendicular vector.
        p = pymunk.Vec2d(-v.y, v.x)
        
        # Compute four vertices representing a rectangle around the segment.
        vertices = [
            A - r * v + p * r,  # Top-left
            B + r * v + p * r,  # Bottom-left
            B + r * v - p * r,   # Bottom-right
            A - r * v - p * r  # Top-right
            
        ]
        return vertices
    
    def end_points(self):
        vertices = self.segment_to_poly()
        end_points = [
            (vertices[0] + vertices[3]) // 2,
            (vertices[1] + vertices[2]) // 2            
             ]
        end_points_local = [self.body.world_to_local(p) for p in end_points]
        return end_points_local
    




