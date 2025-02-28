import pygame as pg
from states.state import State
from states.simple import Simple
import settings

class Title(State):
    def __init__(self, game):
        State.__init__(self,game)

    def update(self, dt, actions):
        if actions["click"]:
            new_state = Simple(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(
            display,
            "Engineered",
            (0,0,0),
            settings.WIDTH/2,
            settings.HEIGHT/2
        )

                    