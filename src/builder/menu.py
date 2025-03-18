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
                border_rect_dims = menu_settings.menu_locations[input['position']]
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
            else:
                self.unrender_button(btn)
        for input in active_menu['inputs']:
            input['input_field'].render(self.game.surface)
                    
    def button_condition_to_render(self,btn):
        condition = btn.get('condition')
        if condition == 0: 
            return True  # always display
        elif condition == 1:
            return self.check_if_at_least_one_component_selected()
        elif condition == 2: 
            return self.check_if_exactly_two_components_selected()
        elif condition == 3:
            return self.check_if_at_least_one_pin_exists()
        elif condition == 4:
            return self.check_if_at_least_one_constraint_in_selected_components() 
        elif condition == 5:
            return self.check_if_at_least_one_pin_in_selected_components()
        elif condition == 6:
            return self.check_if_motor_exists_for_selected_object()


    def check_if_at_least_one_component_selected(self):
        return True if len(self.game.state_stack[-1].manager.selected_components) > 0 else False
        
    def check_if_exactly_two_components_selected(self):
        return True if len(self.game.state_stack[-1].manager.selected_components) == 2 else False
        
    def check_if_at_least_one_pin_exists(self):
        return True if len(self.game.state_stack[-1].manager.pins) > 0 else False
    
    def check_if_at_least_one_constraint_in_selected_components(self):
        selected_components = self.game.state_stack[-1].manager.selected_components
        constraints = self.game.state_stack[-1].manager.constraints
        return any(c for c in constraints for component in selected_components if component == c[1] or component == c[2])
    
    def check_if_at_least_one_pin_in_selected_components(self):
        selected_components = self.game.state_stack[-1].manager.selected_components
        pins = self.game.state_stack[-1].manager.pins
        return any(pin for pin in pins for component in selected_components if component == pin[1])
    
    def check_if_motor_exists_for_selected_object(self):
        selected_components = self.game.state_stack[-1].manager.selected_components
        motors = self.game.state_stack[-1].manager.motors
        return any(motor for motor in motors for component in selected_components if component == motor[1])

    
    def render_button(self,btn):
        location = self.get_button_position(btn)
        radius = menu_settings.button_radius
        color = self.get_button_color(btn)
        font_size = menu_settings.fontsizes['header_2']
        font_color = general_settings.WHITE
        btn['button'] = self.add_button(self.game.surface, location, radius, color, btn['text'], font_size, font_color)

    def unrender_button(self,btn):
        btn['button'] = None

    def get_button_position(self,btn_to_render):
        # give buttons lowest display position available to avoid gaps
        stated_pos_index = btn_to_render.get('position')
        active_menu = self.get_active_menu()
        pos_index = sum([1 for btn in active_menu['buttons'] 
                         if (btn.get('position') < stated_pos_index) 
                         and (self.button_condition_to_render(btn))])
        pos_index += sum([1 for input in active_menu['inputs'] if input.get('position') < stated_pos_index])      
        return menu_settings.menu_locations[pos_index]

    def get_button_color(self,btn): 
        if 'delete' in btn['action']:
            return general_settings.RED
        if btn['target'] != 'main':
            return general_settings.BLUE
        else:
            return general_settings.BLACK
    
    def add_button(self, surface, location, radius, color, text, font_size, font_color):    
        button_rect = pg.draw.rect(surface, color, location, border_radius=radius)
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
                elif action == 'delete_constraints':
                    self.perform_delete_constraints()
                elif action == 'delete_all_pins':
                    self.delete_all_pins()
                elif action == 'delete_selected_pins':
                    self.delete_selected_pins()
                elif action == 'delete_selected_motors':
                    self.delete_selected_motors()
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
        self.game.state_stack[-1].manager.add_component(target)
        
    def perform_delete(self):
        self.game.state_stack[-1].manager.delete_selected_components()

    def perform_delete_constraints(self):
        self.game.state_stack[-1].manager.delete_constraints_from_selected_objects()
    
    def delete_all_pins(self):
        self.game.state_stack[-1].manager.delete_all_pins()

    def delete_selected_pins(self):
        self.game.state_stack[-1].manager.delete_selected_pins()

    def delete_selected_motors(self):
        self.game.state_stack[-1].manager.delete_selected_motors()    

    def load_selected_component_menu(self,component):
        self.navigate_to(component.component_subtype)
        active_menu = self.get_active_menu()
        for idx, input in enumerate(active_menu['inputs']):
            input['input_field'].value = str(component.attributes[idx])

    def assert_exactly_one_active_menu(self):
        active_menus = [key for key, menu in self.menu_map.items() if menu.get('active')]
        assert len(active_menus) == 1, f"Expected exactly one active menu, but found: {active_menus}"
