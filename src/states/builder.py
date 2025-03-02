from states.state import State
import settings
from builder_menu import BuilderMenu  # Assume you saved the menu class in builder_menu.py
from builder_physics import BuilderPhysics  # from physics_environment.py
from builder_objects import Ball

class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Create the separate components
        self.menu = BuilderMenu(game)
        self.physics = BuilderPhysics(game)
    
    def update(self, actions):
        self.physics.update()
        self.menu.update(actions)
        self.game.reset_keys()
    
    def render(self, game):
        game.surface.fill((255, 255, 255))  # Clear the background
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 20)  # Render title
        self.menu.render()
        self.physics.render()

    def add_object(self, target):
        if target == 'ball':
            # For example, add a ball at a default position
            self.ball = Ball(self.game)
            print("Added a ball!")
        else:
            print("Add object target not recognized:", target)
