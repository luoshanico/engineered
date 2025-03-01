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
        self.initialise_menu()      
        self.physics_environment(game)
        

    def update(self, actions):
        # Step the physics space forward (advance simulation)
        self.game.space.step(1 / settings.FPS)
        if actions["click"]:
            self.mouseclick()
        self.game.reset_keys()
    
    def render(self, game):
        self.render_title(game)
        self.render_menu(game)
        game.space.debug_draw(game.draw_options)
        
    def render_title(self,game):
        game.surface.fill((255, 255, 255))  # background color
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 40)  # title text
    
    # MENU #
    ## INITIALISE MENU ##

    def initialise_menu(self):
        self.menu_map = {
            'main': {
                'active': True,
                'buttons': {
                    'object': None,
                    'constraint': None
                }
            },
            'object': {
                'active': False,
                'buttons': {
                    'ball': None,
                    'square': None,
                    'main': None
                }
            },
            'constraint': {
                'active': False,
                'buttons': {
                    'damped_spring': None,
                    'main': None
                }
            }
        }
        self.button_locations = [
            (150, 40, 120, 30),
            (300, 40, 120, 30),
            (450, 40, 120, 30)
        ]
    
    ## RENDER MENU ##

    def render_menu(self,game):
        menu_location = self.get_menu_location()
        
        if menu_location == "main":
            self.render_menu_main(game)
        elif menu_location == "object":
            self.render_menu_object(game)
        elif menu_location == "constraint":
            self.render_menu_constraint(game)
        else:
            raise Exception('Builder menu location is not set to a known location')
    
    def get_menu_location(self):
        self.assert_exactly_one_active_menu_location()
        return next((key for key, value in self.menu_map.items() if value.get('active')), None)
    
    def assert_exactly_one_active_menu_location(self):
        active_locations = [key for key, value in self.menu_map.items() if value.get('active')]
        assert len(active_locations) == 1, f"Expected exactly one active menu location, but found {len(active_locations)}: {active_locations}"
    
    def render_menu_main(self, game):
        self.add_object_button(game)
        self.add_constraint_button(game)
        self.delete_buttons_from_inactive_menus()

    def render_menu_object(self, game):
        self.add_object_ball_button(game)
        self.add_object_back_button(game)
        self.delete_buttons_from_inactive_menus()

    def render_menu_constraint(self, game):
        self.add_constraint_damped_spring_button(game)
        self.add_constraint_back_button(game)
        self.delete_buttons_from_inactive_menus()
        
    ## MENU BUTTONS ##
    ### MAIN MENU BUTTONS ###
    
    def add_object_button(self, game):
        location = self.button_locations[0]
        color = settings.BLUE
        text = "Add Object"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['main']['buttons']['object'] = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_constraint_button(self, game):
        location = self.button_locations[1]
        color = settings.BLUE
        text = "Add Constraint"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['main']['buttons']['constraint'] = utils.add_button(game.surface, location, color, text, font_size, font_color)

    ### OBJECT MENU BUTTONS ###
    
    def add_object_ball_button(self, game):
        location = self.button_locations[0]
        color = settings.GREEN
        text = "Add Ball"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['object']['buttons']['ball'] = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_object_back_button(self, game):
        location = self.button_locations[1]
        color = settings.GREEN
        text = "Back"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['object']['buttons']['main'] = utils.add_button(game.surface, location, color, text, font_size, font_color)
    
    ### CONSTRAINT MENU BUTTONS ###
    
    def add_constraint_damped_spring_button(self, game):
        location = self.button_locations[0]
        color = settings.RED
        text = "Add Spring"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['constraint']['buttons']['damped_spring'] = utils.add_button(game.surface, location, color, text, font_size, font_color)

    def add_constraint_back_button(self, game):
        location = self.button_locations[1]
        color = settings.GREEN
        text = "Back"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['constraint']['buttons']['main'] = utils.add_button(game.surface, location, color, text, font_size, font_color)

    ## MENU UTILS ##

    def get_button_target(self, button):
        for _, info in self.menu_map.items():
            for target, btn in info['buttons'].items():
                if btn is button:
                    return target
        return None
    
    def delete_buttons_from_inactive_menus(self):
        for location in self.menu_map.keys():
            if not self.menu_map[location]['active']:
                for btn in self.menu_map[location]['buttons']:
                    self.menu_map[location]['buttons'][btn] = None
        



    # PHYSICS #
    
    def physics_environment(self,game):
        self.physics_space(game)
        self.add_ground(game)
        self.create_ball(game, pos=(settings.WIDTH // 2, 250))
    
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

    # OBJECTS #
    
    def create_ball(self, game, pos):
        # Create a ball (dynamic body)
        game.ball_mass, game.ball_radius = 1, 60
        game.ball_moment = pymunk.moment_for_circle(game.ball_mass, 0, game.ball_radius)
        game.ball_body = pymunk.Body(game.ball_mass, game.ball_moment)
        game.ball_body.position = pos
        game.ball_shape = pymunk.Circle(game.ball_body, game.ball_radius)
        game.ball_shape.elasticity = 0.9
        game.ball_shape.friction = 0.3
        game.ball_shape.collision_type = settings.OBJECT_CAT
        game.space.add(game.ball_body, game.ball_shape)

    # ACTIONS #
    
    def mouseclick(self):
        mouse_pos = pg.mouse.get_pos()
        menu_location = self.get_menu_location()

        for button in self.menu_map[menu_location]['buttons'].values():
            if button:
                if button.collidepoint(mouse_pos):
                    target = self.get_button_target(button)
                    self.menu_map[target]['active'] = True
                    self.menu_map[menu_location]['active'] = False
                    print(f"Menu location changed from {menu_location} to {target}")


    
    
    