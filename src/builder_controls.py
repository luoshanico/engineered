import pygame as pg
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d
import settings
from builder_objects import Ball
from builder_constraints import DampedSpring



class BuilderControls():
    def __init__(self, game):
        self.game = game
        self.selected_objects = []
        self.mouse_joint = None
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)


    def get_events(self, event):
        
        self.mouse_body.position = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.key.get_mods() & pg.KMOD_CTRL:
                hit, _ = self.get_hit_object_if_dynamic()
                if hit is not None:
                    shape = hit.shape.body
                    if shape not in self.selected_objects:
                        self.selected_objects.append(shape)
                        #shape.color = settings.GREY   
            else:
                self.selected_objects = []
                self.grab_object()
        elif event.type == pg.MOUSEBUTTONUP:
            self.release_object()
            

    def get_hit_object_if_dynamic(self):
        p = Vec2d(*pg.mouse.get_pos())
        hit = self.game.space.point_query_nearest(p, 5, pymunk.ShapeFilter())
        if hit is not None and hit.shape.body.body_type == pymunk.Body.DYNAMIC:
            return hit, p
        else:
            return None, None
    
    
    def grab_object(self):
        if self.mouse_joint is None:  # Only create a new mouse joint if one doesn't already exist.
            hit, p = self.get_hit_object_if_dynamic()
            if hit is not None:
                shape = hit.shape
                # Use the closest point on the shape's surface if needed.
                nearest = hit.point if hit.distance > 0 else p
                self.mouse_joint = pymunk.PivotJoint(
                    self.mouse_body,
                    shape.body,
                    (0, 0),
                    shape.body.world_to_local(nearest),
                )
                self.mouse_joint.max_force = 50000
                self.mouse_joint.error_bias = (1 - 0.15) ** 60
                self.game.space.add(self.mouse_joint)

    def release_object(self):
        if self.mouse_joint is not None:
            self.game.space.remove(self.mouse_joint)
            self.mouse_joint = None
    
    def add_object(self, target):
        if target == 'ball':
            Ball(self.game)
        elif target == 'damped_spring':
            if len(self.selected_objects) == 2:
                DampedSpring(self.game, *self.selected_objects)
            else:
                print("Select exactly two objects to link")
        else:
            print("Add object target not recognized:", target)
    
    def update(self):
        # for things that I want to run once per frame
        pass
