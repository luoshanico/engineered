from builder import objects
from builder import constraints
from builder import pins
from builder import motors

class ComponentManager:
    def __init__(self,game):
        self.game = game
        self.components = []
        self.selected_components = []
        self.constraints = []
        self.pins = []

    def render(self):
        for component in self.components:
            component.render()

    def update(self):
        for component in self.components:
            component.update()
    
    def add_component(self, target):
        print(f"{self.selected_components=}")
        if target == 'ball':
            self.components.append(objects.Ball(self.game))
        elif target == 'bar':
            self.components.append(objects.Bar(self.game))
        elif target == 'motor':
            self.add_motor()
        elif target == 'pin':
            self.add_pin()
        elif target == 'damped_spring':
            if len(self.selected_components) == 2:
                self.components.append(constraints.DampedSpring(self.game, *self.selected_components))
        elif target == 'pin_joint':
            if len(self.selected_components) == 2:
                self.components.append(constraints.PinJoint(self.game, *self.selected_components))
        elif target == 'pivot_joint':
            if len(self.selected_components) == 2:
                self.components.append(constraints.PivotJoint(self.game, *self.selected_components))
        else:
            print("Add object target not recognized:", target)
        self.clear_selected_components()
    
    def add_motor(self):
        for component in self.selected_components:
            if component.component_type == 'object':
                self.components.append(motors.Motor(self.game,component))

    def add_pin(self, component, p):
        if component.component_type == 'object':
            self.components.append(pins.Pins(self.game, component, p))
    
    def render(self):
        for object in self.components:
            object.render(self.game.surface)

    def select_component(self, hit_component):
        self.game.state_stack[-1].menu.load_selected_component_menu(hit_component)
        if hit_component not in self.selected_components:
            self.selected_components.append(hit_component)
            hit_component.apply_selected_color()

    def clear_selected_components(self):
        for component in self.selected_components:
            component.apply_deselected_color()
            component.selected_anchor = None
        self.selected_components = []

    def apply_updated_attributes_to_selected_components(self):
        if len(self.selected_components) > 0:
            updated_subtype = self.selected_components[-1].component_subtype
            for component in self.selected_components:
                if component.component_subtype == updated_subtype:  # only update same subtype
                    component.apply_updated_attributes()
                    self.refresh_constraints(component)
                    self.refresh_pins(component)
                    
                    
                    
    def refresh_constraints(self,component):
        if component.component_type == 'object':
            constraint_data = self.find_components_constraint_data(component)
            for data in constraint_data:
                constraint = data[0]
                constraint.refresh_constraint_after_updated_object()

    def refresh_pins(self,component):
        if component.component_type == 'object':
            pin_data = [pins for pins in self.pins if pins[1]==component]
            for data in pin_data:
                pin = data[0]
                pin.refresh_pin_after_updated_object()


    def store_constraint(self, constraint, obj1, obj2, anchor1, anchor2):
        self.constraints.append((constraint, obj1, obj2, anchor1, anchor2))

    def store_pin(self, pin, obj, anchor):
        self.pins.append((pin, obj, anchor))

    def delete_selected_components(self):
        for component in self.selected_components:
            if component in self.components:
                self.delete_component(component)
        self.clear_selected_components()

    def delete_component(self,component):
        component.delete()
        self.components.remove(component)
        self.remove_constraints(component)
        self.delete_pins_from_component(component)
    
    def delete_constraints_from_selected_objects(self):
        for component in self.selected_components:
            if component.component_type == 'object':
                self.remove_constraints(component)

    def remove_constraints(self,component):
        constraint_data = self.find_components_constraint_data(component)
        if constraint_data:
            if component.component_type == 'constraint':  # remove constraint from constraint listing
                for data in constraint_data:
                    self.constraints.remove(data)
            elif component.component_type == 'object':  # delete constraint
                for data in constraint_data:
                    constraint = data[0]
                    self.delete_component(constraint)

    def find_components_constraint_data(self,component):
        return [c for c in self.constraints if c[0] == component or c[1] == component or c[2] == component]
    
    def delete_pins_from_component(self,component):
        pin_data = [p for p in self.pins if p[1] == component]
        if pin_data:
            for data in pin_data:
                pin = data[0]
                self.delete_component(pin)
                print(f"{self.pins=}")
                print(f"{pin_data=}")
                print(f"{pin=}")
                self.pins.remove(data)

    def delete_all_pins(self):
        for pin_data in self.pins:
            pin = pin_data[0]
            self.delete_component(pin)
        self.pins = []

    def delete_selected_pins(self):
        for component in self.selected_components:
            self.delete_pins_from_component(component)





