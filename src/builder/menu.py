import pygame as pg
from settings import menu_settings
from settings import general_settings
from builder.menu_text import MenuText
from builder.menu_button import Button
from builder.menu_input import InputField



class BuilderMenu:
    def __init__(self, game):
        self.game = game
        self.menu_map = menu_settings.menu_map
        self.initialise_text()
        self.initialse_buttons()
        self.initialise_input_fields()
        self.calculate_menu_positions()
    
    def initialse_buttons(self):
        for _, menu in self.menu_map.items():
            for button in menu['buttons']:
                button['object'] = Button(
                    self.game,
                    button
                )
    
    def initialise_input_fields(self):
        for _, menu in self.menu_map.items():
            for input in menu['inputs']:
                input_name = input['input']
                default_value = input['default_value']
                input['object'] = InputField(
                    self.game,
                    input_name,
                    default_value
                )

    def render(self):
        active_menu = self.get_active_menu()
        for category in ['text','buttons','inputs']:
            for item in active_menu[category]:
                if self.check_condition_to_render(item):
                    item.render()

                    
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
    
    def calculate_menu_positions(self):
        active_menu = self.get_active_menu()
        for category in ['text', 'buttons', 'inputs']: 
            items = active_menu.get(category, [])
            
            # Filter items that should render.
            filtered_items = [item for item in items if self.check_condition_to_render(item)]
            
            # Assign new sequential positions
            for pos, item in enumerate(filtered_items):
                item['object'].get_position(pos)
                
    
    def handle_click(self): 
        mouse_pos = pg.mouse.get_pos()
        active_menu = self.get_active_menu()
        for btn_info in active_menu['buttons']:
            btn_shape = btn_info.get('button').shape
            if btn_shape and btn_shape.collidepoint(mouse_pos):
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
                self.game.state_stack[-1].menu_manager.mark_dirty()

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
