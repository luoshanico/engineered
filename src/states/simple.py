import pygame as pg
from states.state import State
import settings


class Simple(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, dt, actions):
        if actions["click"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(
            display,
            "Simple",
            (255,0,0),
            settings.WIDTH/2,
            settings.HEIGHT/2
        )