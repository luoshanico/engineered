import pygame as pg
from states.state import State
from builder_menu import BuilderMenu
from builder_physics import BuilderPhysics 
from builder_controls import BuilderControls
from builder_objects import BuilderObjects


class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Create the separate components
        self.menu = BuilderMenu(game)
        self.physics = BuilderPhysics(game)
        self.controls = BuilderControls(game)
        self.objects = BuilderObjects(game)

    
    def get_events(self, event):
        self.physics.get_events(event)
        self.menu.get_events(event)
        if not self.menu.event_was_menu_button_hit: 
            self.controls.get_events(event)
        
    def update(self):
        self.physics.update()
        self.controls.update()
        self.menu.update()
        
    def render(self, game):
        game.surface.fill((255, 255, 255))  # Clear the background
        game.draw_text(game.surface, "Builder", (0, 0, 0), 50, 20)  # Render title
        self.menu.render()
        self.physics.render()
        self.objects.render()

    def add_object(self, target):
        self.controls.add_object(target)

