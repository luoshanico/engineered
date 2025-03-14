import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
from pymunk.vec2d import Vec2d


class ComponentControls:
    def __init__(self,game):
        self.game = game
        self.mouse_joint = None
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    def get_events(self, event):
        self.mouse_body.position = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            # print(f"{self.game.state_stack[-1].manager.components}")
            self.handle_mouse_press()
        elif event.type == pg.MOUSEBUTTONUP:
            self.release_component()
            
    def handle_mouse_press(self):
        if pg.key.get_mods() & pg.KMOD_CTRL:
            self.handle_select_action()
        else:
            self.grab_component()

    def handle_select_action(self):
        hit, _ = self.get_hit_component_if_dynamic()
        # print(f"{hit}")
        if hit is not None:
            hit_component = getattr(hit.shape, 'owner', None)
            #print(f"{hit_component=}") 
            self.game.state_stack[-1].manager.select_component(hit_component)
        else:
            self.game.state_stack[-1].manager.clear_selected_components()
    
    def get_hit_component_if_dynamic(self):
        p = Vec2d(*pg.mouse.get_pos())
        filter = pymunk.ShapeFilter()
        nearby_shapes = self.game.space.point_query(p, 5, filter)
        if nearby_shapes:
            hit = min(nearby_shapes, key=lambda info: info.distance)
        else:
            hit = None

        if hit is not None and hit.shape.body.body_type == pymunk.Body.DYNAMIC:
            return hit, p
        else:
            return None, None
    
    def grab_component(self):
        if self.mouse_joint is None:  # Only create a new mouse joint if one doesn't already exist.
            hit, p = self.get_hit_component_if_dynamic()
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

    def release_component(self):
        if self.mouse_joint is not None:
            self.game.space.remove(self.mouse_joint)
            self.mouse_joint = None

    