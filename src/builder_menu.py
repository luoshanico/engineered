import pygame as pg
import settings, utils

class BuilderMenu:
    def __init__(self, game):
        self.game = game
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
    
    def render(self):
        # Render the menu depending on current active section.
        menu_location = self.get_menu_location()
        if menu_location == "main":
            self.render_menu_main()
        elif menu_location == "object":
            self.render_menu_object()
        elif menu_location == "constraint":
            self.render_menu_constraint()
        else:
            raise Exception("Unknown menu location")
    
    def update(self, actions):
        if actions["click"]:
            self.handle_click()
    
    def get_menu_location(self):
        self.assert_exactly_one_active_menu_location()
        return next((key for key, value in self.menu_map.items() if value.get('active')), None)
    
    def assert_exactly_one_active_menu_location(self):
        active_locations = [key for key, value in self.menu_map.items() if value.get('active')]
        assert len(active_locations) == 1, f"Expected exactly one active menu location, but found {len(active_locations)}: {active_locations}"
    
    def render_menu_main(self):
        self.add_object_button()
        self.add_constraint_button()
        self.delete_buttons_from_inactive_menus()
    
    def render_menu_object(self):
        self.add_object_ball_button()
        self.add_object_back_button()
        self.delete_buttons_from_inactive_menus()
    
    def render_menu_constraint(self):
        self.add_constraint_damped_spring_button()
        self.add_constraint_back_button()
        self.delete_buttons_from_inactive_menus()
    
    # Define methods for adding buttons (wrapping utils.add_button)
    def add_object_button(self):
        location = self.button_locations[0]
        color = settings.BLUE
        text = "Add Object"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['main']['buttons']['object'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def add_constraint_button(self):
        location = self.button_locations[1]
        color = settings.BLUE
        text = "Add Constraint"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['main']['buttons']['constraint'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def add_object_ball_button(self):
        location = self.button_locations[0]
        color = settings.GREEN
        text = "Add Ball"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['object']['buttons']['ball'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def add_object_back_button(self):
        location = self.button_locations[1]
        color = settings.GREEN
        text = "Back"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['object']['buttons']['main'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def add_constraint_damped_spring_button(self):
        location = self.button_locations[0]
        color = settings.RED
        text = "Add Spring"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['constraint']['buttons']['damped_spring'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def add_constraint_back_button(self):
        location = self.button_locations[1]
        color = settings.GREEN
        text = "Back"
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        self.menu_map['constraint']['buttons']['main'] = utils.add_button(self.game.surface, location, color, text, font_size, font_color)
    
    def handle_click(self):
        mouse_pos = pg.mouse.get_pos()
        current_location = self.get_menu_location()
        for button in self.menu_map[current_location]['buttons'].values():
            if button and button.collidepoint(mouse_pos):
                target = self.get_button_target(button)
                self.menu_map[target]['active'] = True
                self.menu_map[current_location]['active'] = False
                print(f"Menu location changed from {current_location} to {target}")
    
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
