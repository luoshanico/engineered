from builder import objects
from builder import constraints

class ComponentManager:
    def __init__(self,game):
        self.game = game
        self.components = []
        self.selected_components = []

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
    
    def delete_selected_components(self):
        for component in self.selected_components:
            component.delete()
            self.components.remove(component)
        self.clear_selected_components()

    def render(self):
        for object in self.components:
            object.render(self.game.surface)

    def select_component(self, hit_component):
        if hit_component is not None:
            self.game.state_stack[-1].menu.load_selected_component_menu(hit_component)
            if hit_component not in self.selected_components:
                self.selected_components.append(hit_component)
                hit_component.apply_selected_color()

    def clear_selected_components(self):
        for component in self.selected_components:
            component.apply_deselected_color()
        self.selected_components = []

    def apply_updated_attributes_to_selected_components(self):
        if len(self.selected_components) > 0:
            lastly_selected_component_type = self.selected_components[-1].component_type
            for component in self.selected_components:
                if component.component_type == lastly_selected_component_type:
                    component.apply_updated_attributes(self.game)