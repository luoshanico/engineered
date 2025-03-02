import pygame as pg
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d


class BuilderControls():
    def __init__(self, game):
        self.game = game
        self.mouse_joint = None
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    def get_events(self, event):
        
        self.mouse_body.position = pg.mouse.get_pos()  ## maybe put this in a seperate update function

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.mouse_joint is None:  # Only create a new mouse joint if one doesn't already exist.
                p = Vec2d(*pg.mouse.get_pos())
                hit = self.game.space.point_query_nearest(p, 5, pymunk.ShapeFilter())
                if hit is not None and hit.shape.body.body_type == pymunk.Body.DYNAMIC:  # only mousejoint on dynamic objects
                    print("creating mousejoint")
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

        elif event.type == pg.MOUSEBUTTONUP:
            if self.mouse_joint is not None:
                print("removing mousejoint")
                self.game.space.remove(self.mouse_joint)
                self.mouse_joint = None

    def update(self):
        pass
