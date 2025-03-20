import pymunk
import pymunk.pygame_util
import pygame as pg
from settings import settings

class BuilderWorld:
    def __init__(self, game):
        self.game = game
        self.get_settings()
        self.box_segments = []
        self.add_box()    

    def get_settings(self):
        self.elasticity = 0.8
        self.friction = 0.2
        self.x_start = settings.side_bar_width
        self.width, self.height = self.game.RES

    def add_box(self):
        self.box_thickness = 10
        self.box_dims = [
            ((self.x_start+self.box_thickness, self.height-self.box_thickness),(self.width-self.box_thickness, self.height-self.box_thickness)),  # floor
            ((self.x_start+self.box_thickness, 0+self.box_thickness),(self.width-self.box_thickness, 0+self.box_thickness)),  # ceiling
            ((self.width-self.box_thickness, 0+self.box_thickness),(self.width-self.box_thickness, self.height-self.box_thickness)),  # right wall
            ((self.x_start+self.box_thickness, 0+self.box_thickness),(self.x_start+self.box_thickness, self.height-self.box_thickness)),  # left wall
            ]
        for dims in self.box_dims:
            self.add_segment(dims)

    def add_segment(self,dims):
        shape = pymunk.Segment(
            self.game.space.static_body,
            *dims,
            self.box_thickness
            )
        shape.elasticity = self.elasticity
        shape.friction = self.friction
        shape.collision_type = settings.WORLD_CAT
        self.box_segments.append(shape)
        self.game.space.add(shape)

    def render(self):
        self.render_side_bar()
        for segment in self.box_segments:
            self.render_segment(segment)

    def render_side_bar(self):
        side_bar_dims = ((0,0),(settings.side_bar_width,0),(settings.side_bar_width,self.height),(0,self.height))
        pg.draw.polygon(self.game.surface, settings.DARK_BLUE, side_bar_dims)


    def render_segment(self,segment):
        vertices = self.segment_to_poly(segment)
        points = [(int(v.x), int(v.y)) for v in vertices]
        pg.draw.polygon(self.game.surface, settings.DARK_BLUE, points)
    
    def segment_to_poly(self,segment):
        # Get endpoints in world coordinates.
        A = segment.body.local_to_world(segment.a)
        B = segment.body.local_to_world(segment.b)
        r = segment.radius
        
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
    
    
    def get_events(self,event):
        pass
    
    def update(self):
        pass