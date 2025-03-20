import pygame as pg
from states.state import State
from states.controls import Controls
from settings import settings

class Title(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.game = game

    def get_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            print("Loading Controls State")
            new_state = Controls(self.game)
            new_state.enter_state()
    
    def update(self):
        pass

    def render(self):
        self.game.surface.fill(settings.DARK_BLUE)
        self.draw_title()

    def draw_title(self):
        text = 'Engineered'
        colour = settings.GREEN
        fontsize = 65
        font = self.game.assets.get_font('Advent-Bold',fontsize)
        location = (self.game.width/2, self.game.height/3)
        self.game.draw_text(self.game.surface, text, font, colour, location)

    

                    