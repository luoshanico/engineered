import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
import settings.general
import settings.colours

class BuilderObjects:
    def __init__(self,game):
        self.game = game
        self.objects = []

    def render(self):
        for object in self.objects:
            object.render(self.game.surface)

    def update_default_values(self):
        # self.attributes = ..
        pass


class Ball:
    def __init__(self,game):
        self.pos = (settings.general.loading_bay['width'] // 2, 250)
        self.mass = 1
        self.radius = 60
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = self.pos
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.9
        self.shape.friction = 0.3
        self.color = settings.colours.BLACK
        self.shape.collision_type = settings.general.OBJECT_CAT
        game.space.add(self.body, self.shape)
        game.ball_body = self.body
        game.ball_shape = self.shape

    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))
        


class Rectangle:
    def __init__(self, game):
        self.pos = (settings.general.loading_bay['width'] // 2, 250)
        self.size = self.width, self.height = 20,60
        self.mass = 1
        self.moment = pymunk.moment_for_box(self.mass, self.size)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = self.pos
        self.body.angle = 0
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        self.color = settings.colours.RED
        self.shape.collision_type = settings.general.OBJECT_CAT
        game.space.add(self.body, self.shape)

    def render(self, surface):
        vertices = self.shape.get_vertices()
        vertices = [v.rotated(self.body.angle) + self.body.position for v in vertices]
        points = [(int(v.x), int(v.y)) for v in vertices]
        pg.draw.polygon(surface, self.color, points)
