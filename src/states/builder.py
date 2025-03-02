from states.state import State
import settings
from builder_menu import BuilderMenu  # Assume you saved the menu class in builder_menu.py
from builder_environment import BuilderEnvironment  # from physics_environment.py

class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Create the separate components
        self.menu = BuilderMenu(game)
        self.physics = BuilderEnvironment(game)
        self.physics.add_ground()
        self.physics.create_ball((settings.WIDTH // 2, 250))
    
    def update(self, actions):
        self.physics.update()
        self.menu.update(actions)
        self.game.reset_keys()
    
    def render(self, game):
        game.surface.fill((255, 255, 255))  # Clear the background
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 40)  # Render title
        self.menu.render()
        self.physics.render()
