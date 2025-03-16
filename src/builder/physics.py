import pymunk
import pymunk.pygame_util
import settings.general_settings

class BuilderPhysics:
    def __init__(self, game):
        self.game = game
        self.setup_space()

    def setup_space(self):
        self.game.draw_options = pymunk.pygame_util.DrawOptions(self.game.surface)
        self.game.space = pymunk.Space()
        self.game.space.gravity = 0, 2000

    def get_events(self,event):
        pass
    
    def update(self):
        self.game.space.step(1 / self.game.FPS)

    def render(self):
        for shape in self.game.space.shapes:
            if shape.sensor:
                self.game.space.remove(shape)
        self.game.space.debug_draw(self.game.draw_options)
        for component in self.game.state_stack[-1].manager.components:
            if component.component_type == 'constraint':
                self.game.space.add(component.shape)
