import pygame as pg
from states.state import State
from states.builder import Builder
from settings import settings

class Controls(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.game = game
        self.get_text()

    def get_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if isinstance(self.prev_state,Builder):
                self.prev_state.enter_state()
            else:
                new_state = Builder(self.game)
                new_state.enter_state()
    
    def update(self):
        pass

    def render(self):
        self.draw_background()
        self.draw_title()
        self.draw_controls()

    def draw_background(self):
        self.game.surface.fill(settings.DARK_BLUE)

    def draw_title(self):
        title = 'Controls'
        colour = settings.GREEN
        fontsize = 50
        font = self.game.assets.get_font('Advent-Bold',fontsize)
        location = (self.game.width/2, self.game.height*1/3)
        self.game.draw_text(self.game.surface, title, font, colour, location)

    def draw_controls(self):
        colour = settings.GREY
        fontsize = 26
        font = self.game.assets.get_font('Roobert-SemiBold',fontsize)
        for idx, line in enumerate(self.text):
            location = (self.game.width/2, self.game.height*1/3 + 70 + 50*idx)
            self.game.draw_text(self.game.surface, line, font, colour, location)


    def get_text(self):
        self.text = [
            'Left click: grab object',
            'Ctrl-left-click: select object, place anchor point',
            'Space bar: pin grabbed object to background',
            'Delete: delete object'
        ]

    

    

                    