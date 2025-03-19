import pygame as pg
from settings import menu_map
from settings import settings
from builder.menu_text import MenuText
from builder.menu_button import Button
from builder.menu_input import InputField



class BuilderMenu:
    def __init__(self, game):
        self.game = game
        self.menu_map = menu_map.menu_map
        self.get_menu_dimensions()
        self.initialise_text()
        self.initialse_buttons()
        self.initialise_input_fields()    
    
    def get_menu_dimensions(self):
        menu_dims = settings.menu_dims
        max_buttons = (settings.HEIGHT - menu_dims['button_start_y']) // (menu_dims['button_height'] + menu_dims['button_gap'])
        self.menu_positions = [(menu_dims['button_start_x'], menu_dims['button_start_y'] 
                                + i * (menu_dims['button_height'] + menu_dims['button_gap']), 
                                menu_dims['button_width'], menu_dims['button_height'])
                                for i in range(max_buttons)]
    
    def initialise_text(self):
        for _, menu in self.menu_map.items():
            for menu_item in menu['items']:
                if menu_item['type'] == 'text':
                    menu_item['object'] = MenuText(self.game,menu_item)
    
    def initialse_buttons(self):
       for _, menu in self.menu_map.items():
            for menu_item in menu['items']:
                if menu_item['type'] == 'button':
                    menu_item['object'] = Button(self.game,menu_item)

    
    def initialise_input_fields(self):
        for _, menu in self.menu_map.items():
            for menu_item in menu['items']:
                if menu_item['type'] == 'input':
                    menu_item['object'] = InputField(self.game,menu_item)

    def render(self):
        for menu_item in self.get_active_menu()['items']:
            if self.check_condition_to_render(menu_item):
                if menu_item['object']:
                    menu_item['object'].render()

                    
    def check_condition_to_render(self,menu_item):
        condition = menu_item.get('condition')
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
        elif condition == 7:
            return not self.check_if_at_least_one_component_selected() # only show if nothing selected


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
    
    

    def get_events(self,event):
        active_menu = self.get_active_menu()
        for item in active_menu['items']:
            if item['type'] == 'input':
                item['object'].get_events(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            self.handle_click()
        
    def update(self):
        pass

    def get_active_menu(self):
        self.assert_exactly_one_active_menu()
        for _, menu_item in self.menu_map.items():
            if menu_item.get('active'):
                return menu_item
        return None
    
    def calculate_menu_positions(self):
        active_menu = self.get_active_menu()
        filtered_items = [item for item in active_menu['items'] if self.check_condition_to_render(item)]
        for pos_idx, item in enumerate(filtered_items):
            item['object'].get_position(pos_idx)
                
    
    def handle_click(self): 
        mouse_pos = pg.mouse.get_pos()
        active_menu = self.get_active_menu()
        for item in active_menu['items']:
            if item['type'] == 'button':
                btn_shape = item.get('object').shape
                if btn_shape and btn_shape.collidepoint(mouse_pos):
                    action = item.get('action')
                    target = item.get('target')

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
                    self.game.state_stack[-1].menu_manager.mark_dirty()

    def navigate_to(self, target):
        # Deactivate all menus
        for key in self.menu_map:
            self.menu_map[key]['active'] = False
        if target in self.menu_map:
            self.menu_map[target]['active'] = True

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
        active_inputs = [items for items in self.get_active_menu()['items'] if items['type']=='input']
        for idx, item in enumerate(active_inputs):
            item['object'].value = str(component.attributes[idx])

    def assert_exactly_one_active_menu(self):
        active_menus = [key for key, menu in self.menu_map.items() if menu.get('active')]
        assert len(active_menus) == 1, f"Expected exactly one active menu, but found: {active_menus}"
