import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
pymunk.pygame_util.positive_y_is_up = False
import settings
from states.main_menu import Title


class Game():
    def __init__(self):
        pg.init()

        self.surface = pg.Surface(settings.RES)
        print(f"{settings.RES=}")
        self.screen = pg.display.set_mode(settings.RES)
        self.running, self.playing = True, True
        print("init called, resetting keys")
        self.clock = pg.time.Clock()
        self.dt = 0
        self.font = pg.font.Font(None, settings.fontsizes['title'])

        self.state_stack = []

        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:
            # self.get_dt()
            self.get_events()
            self.update()
            self.render()
            self.clock.tick(settings.FPS)

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            self.state_stack[-1].get_events(event)

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render(self)
        self.screen.blit(self.surface, (0,0))
        pg.display.flip()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        pass

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
        print(self.state_stack[-1])


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()


