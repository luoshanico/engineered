from builder import objects
from builder import constraints

class ComponentManager:
    def __init__(self,game):
        self.game = game
        self.components = []
        self.selected_components = []
        self.constraints = []

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
        elif target == 'rectangle':
            self.components.append(objects.Rectangle(self.game))
        elif target == 'damped_spring':
            if len(self.selected_components) == 2:
                self.components.append(constraints.DampedSpring(self.game, *self.selected_components))
            else:
                print("Select exactly two objects to link")
        else:
            print("Add object target not recognized:", target)
        self.clear_selected_components()
    
    
    def render(self):
        for object in self.components:
            object.render(self.game.surface)

    def select_component(self, hit_component):
        self.game.state_stack[-1].menu.load_selected_component_menu(hit_component)
        if hit_component not in self.selected_components:
            self.selected_components.append(hit_component)
            hit_component.apply_selected_color()
            self.clear_anchors_if_over_two_selected()

    def clear_anchors_if_over_two_selected(self):
        if len(self.selected_components) > 2:
            for component in self.selected_components:
                component.selected_anchor = None

    def clear_selected_components(self):
        for component in self.selected_components:
            component.apply_deselected_color()
            component.selected_anchor = None
        self.selected_components = []

    def apply_updated_attributes_to_selected_components(self):
        if len(self.selected_components) > 0:
            lastly_selected_component_subtype = self.selected_components[-1].component_subtype
            for component in self.selected_components:
                if component.component_subtype == lastly_selected_component_subtype:  
                    # e.g. if the last item I selected was a ball then update all selected balls
                    # but do not update any selected springs or update any unselected balls
                    component.apply_updated_attributes()
                    if component.component_type == 'object':
                        constraint_data = self.find_components_constraint_data(component)
                        constraint = constraint_data[0]
                        constraint.refresh_constraint_after_updated_object()


    def store_constraint(self, constraint, obj1, obj2, anchor1, anchor2):
        self.constraints.append((constraint, obj1, obj2, anchor1, anchor2))

    def delete_selected_components(self):
        for component in self.selected_components:
            if component in self.components:
                self.delete_component(component)
        self.clear_selected_components()

    def delete_component(self,component):
        component.delete()
        self.components.remove(component)
        self.remove_constraint(component)
    
    def remove_constraint(self,component):
        constraint_data = self.find_components_constraint_data(component)
        if constraint_data:
            if component.component_type == 'constraint':  # remove constraint from constraint listing
                self.constraints.remove(constraint_data)
        elif component.component_type == 'object':  # delete constraint
            constraint = constraint_data[0]
            self.delete_component(constraint)

    def find_components_constraint_data(self,component):
        constraint_data = next((c for c in self.constraints if c[0] == component), None)
        if not constraint_data:
            constraint_data = next((c for c in self.constraints if c[1] == component), None)
        if not constraint_data:
            constraint_data = next((c for c in self.constraints if c[2] == component), None)
        return constraint_data





