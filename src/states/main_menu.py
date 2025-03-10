import pygame as pg
from states.state import State
from states.builder import Builder
import settings.general_settings

class Title(State):
    def __init__(self, game):
        State.__init__(self,game)

    def get_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            print("updating to Builder")
            new_state = Builder(self.game)
            new_state.enter_state()
    
    def update(self):
        pass

    def render(self, game):
        game.surface.fill((255,255,255))
        self.game.draw_text(
            game.surface,
            "Engineered",
            (0,0,0),
            settings.general_settings.WIDTH/2,
            settings.general_settings.HEIGHT/2
        )

                    