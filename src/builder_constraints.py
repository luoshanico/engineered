import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
from pymunk.vec2d import Vec2d
import settings.menu_settings as menu_settings

class Constraints:
    def __init__(self,game):
        self.game = game
        self.constraints = []
        self.selected_constraints = []
        self.mouse_joint = None
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    def render(self):
        for constraint in self.constraints:
            constraint.render(self.game.surface)

    def update_default_values(self):
        # self.attributes = ..
        pass

    def get_events(self, event):
        self.mouse_body.position = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.key.get_mods() & pg.KMOD_CTRL:
                hit, _ = self.get_hit_constraint_if_dynamic()
                if hit is not None:
                    shape = hit.shape.body
                    print(f"selected constraint {shape}")
                    if shape not in self.selected_constraints:
                        self.selected_constraints.append(shape)
                        #shape.color = settings.GREY   


    def get_hit_constraint_if_dynamic(self):
        p = Vec2d(*pg.mouse.get_pos())
        hit = self.game.space.point_query_nearest(p, 5, pymunk.ShapeFilter())
        if hit is not None and hit.shape.body.body_type == pymunk.Body.DYNAMIC:
            return hit, p
        else:
            return None, None
    
    def update(self):
        # for things that I want to run once per frame
        pass


class DampedSpring:
    def __init__(self, game, obj1, obj2):
        self.spring = pymunk.DampedSpring(obj1.shape, obj2.shape, (60, 0), (-60, 0), 20, 5, 0.3)
        game.space.add(self.spring)

    def render(self, surface):
        # if you want to add pg shape over the constraint
        pass