from states.state import State
import settings, utils

import pymunk
import pygame as pg

class Builder(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

        title_font = pg.font.Font(None, settings.fontsizes['title'])
        text = title_font.render("Builder", True, settings.BLACK)
        screen.blit(text, (10, 10))

        # Add object button
        location = (150, 40, 140, 30)
        color = settings.BLUE
        text = "Add Object"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        object_button = utils.add_button(screen, location, color, text, font_size, font_color)

        # Add constraint Button
        location = (320, 40, 140, 30)
        color = settings.BLUE
        text = "Add Constraint"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        constraint_button = utils.add_button(screen, location, color, text, font_size, font_color)

        # Initialize the physics space
        self.draw_options = pymunk.pygame_util.DrawOptions(self.surface)
        self.space = pymunk.Space()
        self.space.gravity = 0, 2000

        # Add the ground
        self.segment_shape = pymunk.Segment(self.space.static_body, (0, settings.HEIGHT), (settings.RES), 20)
        self.segment_shape.elasticity = settings.world['elasticity']
        self.segment_shape.friction = settings.world['friction']
        self.segment_shape.collision_type = settings.WORLD_CAT
        self.space.add(self.segment_shape)

        # Global variables
        self.selected_object_1 = None
        self.selected_object_2 = None
        
        
        return object_button, constraint_button

    def update(self, dt, actions):
        self.game.reset_keys()