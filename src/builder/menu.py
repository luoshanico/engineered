import pygame as pg
from settings import menu_settings
from settings import general_settings
from builder.input_field import InputField

class BuilderMenu:
    def __init__(self, game):
        self.game = game
        self.menu_map = menu_settings.menu_map
        self.initialise_input_fields()
    
    def initialise_input_fields(self):
        for key, menu in self.menu_map.items():
            for input in menu['inputs']:
                border_rect_dims = menu_settings.input_locations[input['position']]
                input_name = input['input']
                default_value = input['default_value']
                input['input_field'] = InputField(
                    self.game,
                    border_rect_dims,
                    input_name,
                    default_value
                )

    def render(self):
        active_menu = self.get_active_menu()
        for btn in active_menu['buttons']:
            if self.button_condition_to_render(btn):
                self.render_button(btn)
        for input in active_menu['inputs']:
            input['input_field'].render(self.game.surface)
                    
    def button_condition_to_render(self,btn):
        condition = btn.get('condition')
        if condition == 0:  # no condition ,always display
            return True
        elif condition == 1:  # display if objects selected
            if len(self.game.state_stack[-1].objects.manager.selected_objects) > 0:
                return True
            else:
                return False
        elif condition == 2:  # display if exactly 2 objects selected (for adding constraints)
            if len(self.game.state_stack[-1].objects.manager.selected_objects) == 2:
                return True
            else:
                return False 
            

    
    def render_button(self,btn):
        location = self.get_button_position(btn)
        color = self.get_button_color(btn)
        font_size = menu_settings.fontsizes['header_2']
        font_color = general_settings.WHITE
        btn['button'] = self.add_button(self.game.surface, location, color, btn['text'], font_size, font_color)

    def get_button_position(self,btn_to_render):
        # give buttons lowest display position available to avoid gaps
        pos_index = btn_to_render.get('position')
        active_menu = self.get_active_menu()
        pos_index = sum([1 for btn in active_menu['buttons'] 
                         if (btn.get('position') < pos_index) 
                         and (self.button_condition_to_render(btn))])      
        return menu_settings.button_locations[pos_index]

    def get_button_color(self,btn): 
        if btn['action'] == 'delete':
            return general_settings.RED
        if btn['target'] != 'main':
            return general_settings.BLUE
        else:
            return general_settings.BLACK
    
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
                action = btn_info.get('action')
                target = btn_info.get('target')
                if action == 'nav':
                    self.navigate_to(target)
                elif action == 'add':
                    self.perform_add(target)
                elif action == 'delete':
                    self.perform_delete()
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
        self.game.state_stack[-1].objects.manager.add_object(target)
        

    def perform_delete(self):
        self.game.state_stack[-1].objects.manager.delete_selected_objects()

    def load_selected_object_menu(self,object):
        self.navigate_to(object.object_type)
        active_menu = self.get_active_menu()
        for idx, input in enumerate(active_menu['inputs']):
            input['input_field'].value = str(object.attributes[idx])

    def assert_exactly_one_active_menu(self):
        active_menus = [key for key, menu in self.menu_map.items() if menu.get('active')]
        assert len(active_menus) == 1, f"Expected exactly one active menu, but found: {active_menus}"
