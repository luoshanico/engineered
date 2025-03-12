import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
from pymunk.vec2d import Vec2d
from settings import general_settings
from settings.menu_settings import menu_map
from builder_constraints import DampedSpring
from collections import namedtuple
import utils

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

    def get_events(self, event):
        self.mouse_body.position = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            self.handle_mouse_press()
        elif event.type == pg.MOUSEBUTTONUP:
            self.release_object()
            
    def handle_mouse_press(self):
        if pg.key.get_mods() & pg.KMOD_CTRL:
            self.handle_select_action()
        else:
            self.grab_object()

    def handle_select_action(self):
        hit, _ = self.get_hit_object_if_dynamic()
        if hit is not None:
            hit_object = getattr(hit.shape, 'owner', None) 
            self.select_object(hit_object)
            
        else:
            self.clear_selected_objects()

    def select_object(self, hit_object):
        if hit_object is not None:
            self.game.state_stack[-1].menu.load_selected_object_menu(hit_object)
            if hit_object not in self.selected_objects:
                self.selected_objects.append(hit_object)
                hit_object.apply_color_to_indicate_selected()

    def clear_selected_objects(self):
        for object in self.selected_objects:
            object.apply_deselected_color()
        self.selected_objects = []
        
    
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
        pass

    def apply_updated_attributes_to_selected_objects(self):
        print(f"{self.selected_objects=}, {self.objects=}")
        if len(self.selected_objects) > 0:
            lastly_selected_object_type = self.selected_objects[-1].object_type
            for object in self.selected_objects:
                if object.object_type == lastly_selected_object_type:
                    object.apply_updated_attributes(self.game)
            


class Ball:
    def __init__(self,game):
        self.game = game
        self.get_attributes()
        self.create_body()
        self.create_shape()
        self.add_labels()
        self.get_initial_position()
        self.get_initial_color()
        self.add_to_space()
        
        
    def get_initial_position(self):
        self.body.position = (general_settings.loading_bay['width'] // 2, 250)
    
    def get_attributes(self):
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
    
    def add_to_space(self):
        self.game.space.add(self.body, self.shape)
        self.game.ball_body = self.body
        self.game.ball_shape = self.shape
        
    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))

    def apply_updated_attributes(self, game):
        self.store_current_position()
        self.remove_existing_object()
        self.get_attributes()
        self.create_body()
        self.create_shape()
        self.restore_position()
        self.add_to_space()

    def remove_existing_object(self):
        self.game.space.remove(self.body, self.shape)
    
    def store_current_position(self):
        pos = self.body.position
        self.current_position = (int(pos.x), int(pos.y))

    def restore_position(self):
        self.body.position = self.current_position

    def apply_color_to_indicate_selected(self):
        self.normal_rgb = self.color
        self.color = utils.fade_color(self.color)

    def apply_deselected_color(self):
        self.color = self.normal_rgb


        
        


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
