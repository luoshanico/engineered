import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
from pymunk.vec2d import Vec2d
from settings import general_settings
from settings.menu_settings import menu_map
from builder_constraints import DampedSpring

class BuilderObjects:
    def __init__(self,game):
        self.game = game
        self.objects = []
        self.selected_objects = []
        self.mouse_joint = None
        self.mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    def render(self):
        for object in self.objects:
            object.render(self.game.surface)

    def update_default_values(self):
        # self.attributes = ..
        pass

    def get_events(self, event):
        self.mouse_body.position = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.key.get_mods() & pg.KMOD_CTRL:
                hit, _ = self.get_hit_object_if_dynamic()
                if hit is not None:
                    shape = hit.shape
                    if shape not in self.selected_objects:
                        self.selected_objects.append(shape)
                        print(shape.object_type)
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
            self.objects.append(Ball(self.game))
        if target == 'rectangle':
            self.objects.append(Rectangle(self.game))
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


class Ball:
    def __init__(self,game):
        self.pos = (general_settings.loading_bay['width'] // 2, 250)
        self.get_attribute_values()
        self.color = general_settings.BLACK
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = self.pos
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction
        self.shape.collision_type = general_settings.OBJECT_CAT
        self.shape.object_type = 'ball'
        game.space.add(self.body, self.shape)
        game.ball_body = self.body
        game.ball_shape = self.shape

    def get_attribute_values(self):
        self.mass = float(menu_map['ball']['inputs'][0]['input_field'].value)
        self.radius = float(menu_map['ball']['inputs'][1]['input_field'].value)
        self.elasticity = float(menu_map['ball']['inputs'][2]['input_field'].value)
        self.friction = float(menu_map['ball']['inputs'][3]['input_field'].value)

    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))
        


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
