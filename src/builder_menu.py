import pygame as pg
from settings import menu_settings
from settings import general_settings
from builder_input_field import InputField

class BuilderMenu:
    def __init__(self, game):
        self.game = game
        self.menu_map = menu_settings.menu_map
        self.initialise_input_fields()
        self.event_was_menu_button_hit = False
    
    def initialise_input_fields(self):
        for key, menu in self.menu_map.items():
            for input in menu['inputs']:
                border_rect_dims = menu_settings.input_locations[input['position']]
                input_name = input['input']
                default_value = input['default_value']
                input['input_field'] = InputField(
                    border_rect_dims,
                    input_name,
                    default_value
                )


    def render(self):
        active_menu = self.get_active_menu()
        for btn in active_menu['buttons']:
            self.render_button(btn)
        for input in active_menu['inputs']:
            input['input_field'].render(self.game.surface)
                    
    def render_button(self,btn):
        pos_index = btn.get('position')
        location = menu_settings.button_locations[pos_index]
        color = general_settings.BLUE if btn['target'] != 'main' else general_settings.BLACK
        font_size = menu_settings.fontsizes['header_2']
        font_color = general_settings.WHITE
        btn['button'] = self.add_button(self.game.surface, location, color, btn['text'], font_size, font_color)


    def add_button(self, surface, location, color, text, font_size, font_color):    
        button_rect = pg.draw.rect(surface, color, location)
        font = pg.font.Font(None, font_size)
        button_text = font.render(text, True, font_color)
        text_location = self.center_text_in_rectangle(location, font_size, text)
        surface.blit(button_text, text_location)
        return button_rect
    

    def center_text_in_rectangle(self, rectangle_dims, font_size, text):
        font = pg.font.Font(None, font_size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()
        x = rectangle_dims[0] + (rectangle_dims[2] - text_width) // 2
        y = rectangle_dims[1] + (rectangle_dims[3] - text_height) // 2
        return (x, y)

    
    def get_events(self,event):
        active_menu = self.get_active_menu()
        for input in active_menu['inputs']:
            input['input_field'].get_events(event)
        self.event_was_menu_button_hit = False
        if event.type == pg.MOUSEBUTTONDOWN:
            self.handle_click()
        
    
    def update(self):
        pass

    def get_active_menu(self):
        self.assert_exactly_one_active_menu()
        for _, menu in self.menu_map.items():
            if menu.get('active'):
                return menu
        return None

    def handle_click(self): 
        mouse_pos = pg.mouse.get_pos()
        active_menu = self.get_active_menu()
        for btn_info in active_menu['buttons']:
            btn = btn_info.get('button')
            if btn and btn.collidepoint(mouse_pos):
                self.event_was_menu_button_hit = True
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
        self.game.state_stack[-1].add_object(target)

    def load_selected_object_menu(self,shape):
        self.navigate_to(shape.object_type)
        active_menu = self.get_active_menu()
        #for i in range(len(active_menu['inputs'])):
            #active_menu['inputs'][i]['input_field'].value = str(shape.attributes[i])

        for idx, input in enumerate(active_menu['inputs']):
            input['input_field'].value = str(shape.attributes[idx])

    def assert_exactly_one_active_menu(self):
        active_menus = [key for key, menu in self.menu_map.items() if menu.get('active')]
        assert len(active_menus) == 1, f"Expected exactly one active menu, but found: {active_menus}"
