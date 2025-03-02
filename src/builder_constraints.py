import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
import settings

class DampedSpring:
    def __init__(self, game, obj1, obj2):
        self.spring = pymunk.DampedSpring(obj1, obj2, (60, 0), (-60, 0), 20, 5, 0.3)
        game.space.add(self.spring)