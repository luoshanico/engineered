from states.state import State
import settings, utils

import pymunk
import pymunk.pygame_util
import pygame as pg

# basic physics space

class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.object_button, self.constraint_button = None, None
        self.ball_button, self.damped_spring_button = None, None
        self.back_button = None
        self.menu_location = "main"
        

    def update(self, dt, actions):
        # Step the physics space forward (advance simulation)
        self.game.space.step(dt)
        if actions["click"]:
            self.mouseclick()
        self.game.reset_keys()
    
    def render(self, game):
        self.builder_title(game)
        self.builder_menu(game)
        self.physics_environment(game)
        game.space.debug_draw(game.draw_options)
    
    def builder_title(self,game):
        game.surface.fill((255, 255, 255))  # background color
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 40)  # Title text

    def builder_menu(self,game):
        if self.menu_location == "main":
            self.builder_menu_main(game)
        elif self.menu_location == "object":
            self.builder_menu_object(game)
        elif self.menu_location == "constraint":
            self.builder_menu_constraint(game)
    
    def builder_menu_main(self, game):
        self.add_object_button(game)
        self.add_constraint_button(game)

    def builder_menu_object(self, game):
        self.object_button = None
        self.constraint_button = None
        self.add_ball_button(game)
        self.add_back_button(game)

    def builder_menu_constraint(self, game):
        self.object_button = None
        self.constraint_button = None
        self.add_damped_spring_button(game)
        
    def add_object_button(self, game):
        location = (150, 40, 140, 30)
        color = settings.BLUE
        text = "Add Object"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.object_button = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_constraint_button(self, game):
        location = (320, 40, 140, 30)
        color = settings.BLUE
        text = "Add Constraint"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.constraint_button = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_ball_button(self, game):
        location = (150, 40, 140, 30)
        color = settings.GREEN
        text = "Add Ball"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.ball_button = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_damped_spring_button(self, game):
        location = (150, 40, 140, 30)
        color = settings.RED
        text = "Add Spring"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.damped_spring_button = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_back_button(self, game):
        location = (350, 40, 140, 30)
        color = settings.BLACK
        text = "Back"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.back_button = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def physics_environment(self,game):
        self.physics_space(game)
        self.add_ground(game)
        self.create_ball(game, pos=(settings.WIDTH // 2, settings.HEIGHT - 100))
    
    def physics_space(self, game):
        # Initialize the physics space
        game.draw_options = pymunk.pygame_util.DrawOptions(game.surface)
        game.space = pymunk.Space()
        game.space.gravity = 0, 2000

    def add_ground(self, game):
        # Create a ground (static segment)
        game.segment_shape = pymunk.Segment(game.space.static_body, (0, settings.HEIGHT), (settings.RES), 20)
        game.segment_shape.elasticity = settings.world['elasticity']
        game.segment_shape.friction = settings.world['friction']
        game.segment_shape.collision_type = settings.WORLD_CAT
        game.space.add(game.segment_shape)

    def create_ball(self, game, pos):
        # Create a ball (dynamic body)
        game.ball_mass, game.ball_radius = 1, 60
        game.ball_moment = pymunk.moment_for_circle(game.ball_mass, 0, game.ball_radius)
        game.ball_body = pymunk.Body(game.ball_mass, game.ball_moment)
        game.ball_body.position = pos
        game.ball_shape = pymunk.Circle(game.ball_body, game.ball_radius)
        game.ball_shape.elasticity = 0.8
        game.ball_shape.friction = 0.5
        game.ball_shape.collision_type = settings.OBJECT_CAT
        game.space.add(game.ball_body, game.ball_shape)

    def mouseclick(self):
        mouse_pos = pg.mouse.get_pos()
        if self.object_button is not None:
            if self.object_button.collidepoint(mouse_pos):
                self.menu_location = "object"
                print("Add object...")
        elif self.constraint_button is not None:
            if self.constraint_button.collidepoint(mouse_pos):
                self.menu_location = "constraint"
                print("Add constraint...")
        elif self.back_button is not None:
            if self.back_button.collidepoint(mouse_pos):
                self.menu_location = "main"
                print("Main menu...")
    
    