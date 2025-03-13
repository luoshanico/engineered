from builder import objects

class ObjectManager:
    def __init__(self,game):
        self.game = game
        self.objects = []
        self.selected_objects = []

    def render(self):
        for object in self.objects:
            object.render()

    def update(self):
        for object in self.objects:
            object.update()
    
    def add_object(self, target):
        print(f"{self.selected_objects=}")
        if target == 'ball':
            self.objects.append(objects.Ball(self.game))
        elif target == 'rectangle':
            self.objects.append(objects.Rectangle(self.game))
        elif target == 'damped_spring':
            if len(self.selected_objects) == 2:
                self.objects.append(objects.DampedSpring(self.game, *self.selected_objects))
            else:
                print("Select exactly two objects to link")
        else:
            print("Add object target not recognized:", target)
        self.clear_selected_objects()
    
    def delete_selected_objects(self):
        for object in self.selected_objects:
            object.delete()
            self.objects.remove(object)
        self.clear_selected_objects()

    def render(self):
        for object in self.objects:
            object.render(self.game.surface)

    def select_object(self, hit_object):
        if hit_object is not None:
            self.game.state_stack[-1].menu.load_selected_object_menu(hit_object)
            if hit_object not in self.selected_objects:
                self.selected_objects.append(hit_object)
                hit_object.apply_color_to_indicate_selected()

    def clear_selected_objects(self):
        for object in self.selected_objects:
            object.apply_deselected_color()
        self.selected_objects = []

    def apply_updated_attributes_to_selected_objects(self):
        if len(self.selected_objects) > 0:
            lastly_selected_object_type = self.selected_objects[-1].object_type
            for object in self.selected_objects:
                if object.object_type == lastly_selected_object_type:
                    object.apply_updated_attributes(self.game)