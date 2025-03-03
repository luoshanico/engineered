import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
import settings

class BuilderObjects:
    def __init__(self,game):
        self.game = game
        self.objects = []

    def render(self):
        for object in self.objects:
            object.render(self.game.surface)


class Ball:
    def __init__(self,game):
        self.pos = (settings.loading_bay['width'] // 2, 250)
        self.mass = 1
        self.radius = 60
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = self.pos
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.9
        self.shape.friction = 0.3
        self.shape.collision_type = settings.OBJECT_CAT
        game.space.add(self.body, self.shape)
        game.ball_body = self.body
        game.ball_shape = self.shape

    def render(self, surface):
        pos = self.body.position
        radius = self.radius
        self.color = settings.BLACK
        pg.draw.circle(surface, self.color, (int(pos.x), int(pos.y)), int(radius))
        

