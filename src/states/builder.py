from states.state import State
from builder.menu.menu import BuilderMenu
from builder.physics import BuilderPhysics 
from builder.components.manager import ComponentManager
from builder.components.controls import ComponentControls
from builder.world import BuilderWorld
from builder.menu.menu_manager import MenuManager
from settings import settings


class Builder(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.menu_manager = MenuManager(game)
        self.menu = BuilderMenu(game)
        self.physics = BuilderPhysics(game)
        self.world = BuilderWorld(game)
        self.controls = ComponentControls(game)
        self.manager = ComponentManager(game)
        
    def get_events(self, event):
        self.physics.get_events(event)
        self.menu.get_events(event)
        self.controls.get_events(event)
        self.menu_manager.recalc_if_needed()
        
    def update(self):
        self.physics.update()
        self.manager.update()
        self.menu.update()
        
    def render(self):
        self.game.surface.fill(settings.OFFWHITE)  # Clear the background
        self.physics.render()
        self.manager.render()
        self.world.render()
        self.menu.render()
        self.draw_title()


    def draw_title(self):
        text = 'Engineered'
        colour = settings.GREEN
        fontsize = 30
        font = self.game.assets.get_font('Advent-Bold',fontsize)
        location = (settings.side_bar_width/2, 35)
        self.game.draw_text(self.game.surface, text, font, colour, location)

    
