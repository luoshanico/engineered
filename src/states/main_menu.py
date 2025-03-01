import pygame as pg
from states.state import State
from states.simple import Simple
from states.builder import Builder
import settings

class Title(State):
    def __init__(self, game):
        State.__init__(self,game)

    def update(self, actions):
        if actions["click"]:
            print("updating to Builder")
            new_state = Builder(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, game):
        game.surface.fill((255,255,255))
        self.game.draw_text(
            game.surface,
            "Engineered",
            (0,0,0),
            settings.WIDTH/2,
            settings.HEIGHT/2
        )

                    