import pygame as pg
from states.state import State
from builder.menu import BuilderMenu
from builder.physics import BuilderPhysics 
from builder.manager import ComponentManager
from builder.controls import ComponentControls


class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.menu = BuilderMenu(game)
        self.physics = BuilderPhysics(game)
        self.controls = ComponentControls(game)
        self.manager = ComponentManager(game)
        
    def get_events(self, event):
        self.physics.get_events(event)
        self.menu.get_events(event)
        self.controls.get_events(event)
        
    def update(self):
        self.physics.update()
        self.manager.update()
        self.menu.update()
        
    def render(self, game):
        game.surface.fill((255, 255, 255))  # Clear the background
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 20)  # Render title
        self.menu.render()
        self.physics.render()
        self.manager.render()
