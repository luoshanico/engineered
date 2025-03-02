import pygame as pg
import settings, utils

class BuilderMenu:
    def __init__(self, game):
        self.game = game
        self.menu_map = {
            'main': {
                'active': True,
                'buttons': [
                    {'action': 'nav', 'target': 'object', 'button': None, 'text': 'Add object', 'position': 0},
                    {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1},
                ]
            },
            'object': {
                'active': False,
                'buttons': [
                    {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Ball', 'position': 0},
                    {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Rectangle', 'position': 1},
                    {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Triangle', 'position': 2},
                    {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3}
                ]
            },
            'constraint': {
                'active': False,
                'buttons': [
                    {'action': 'nav', 'target': 'damped_spring', 'button': None, 'text': 'Add spring', 'position': 0},
                    {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 1}
                ]
            }
        }
        self.button_locations = [
            (20, 40, 120, 30),
            (160, 40, 120, 30),
            (300, 40, 120, 30),
            (440, 40, 120, 30)
        ]
    
    def render(self):
        active_menu = self.get_active_menu()
        for btn in active_menu['buttons']:
            self.render_button(btn)
            
            
    def render_button(self,btn):
        pos_index = btn.get('position')
        location = self.button_locations[pos_index]
        color = settings.BLUE if btn['target'] != 'main' else settings.BLACK
        font_size = settings.fontsizes['header_1']
        font_color = settings.WHITE
        btn['button'] = utils.add_button(self.game.surface, location, color, btn['text'], font_size, font_color)

    
    def get_events(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.handle_click()
    
    def update(self):
        pass

    def get_active_menu(self):
        # Return the first menu in menu_map where 'active' is True
        self.assert_exactly_one_active_menu()
        for key, menu in self.menu_map.items():
            if menu.get('active'):
                return menu
        return None

    def handle_click(self):
        mouse_pos = pg.mouse.get_pos()
        active_menu = self.get_active_menu()
        for btn_info in active_menu['buttons']:
            btn = btn_info.get('button')
            if btn and btn.collidepoint(mouse_pos):
                action = btn_info.get('action')
                target = btn_info.get('target')
                if action == 'nav':
                    self.navigate_to(target)
                elif action == 'add':
                    self.perform_add(target)
                break

    def navigate_to(self, target):
        # Deactivate all menus
        for key in self.menu_map:
            self.menu_map[key]['active'] = False
        # If target exists as a menu key, activate it; otherwise, perform other action.
        if target in self.menu_map:
            self.menu_map[target]['active'] = True
        else:
            print("Target is not a menu, perform alternative action:", target)

    def perform_add(self, target):
        builder_state = self.game.state_stack[-1]  # Assuming Builder is active
        builder_state.add_object(target)

    def assert_exactly_one_active_menu(self):
        active_menus = [key for key, menu in self.menu_map.items() if menu.get('active')]
        assert len(active_menus) == 1, f"Expected exactly one active menu, but found: {active_menus}"
