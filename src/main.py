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
        self.actions = {'click':False}
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
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button press
                    self.actions['click'] = True

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.state_stack[-1].render(self)
        self.screen.blit(self.surface, (0,0))
        pg.display.flip()

    #def get_dt(self):
        #self.dt = self.clock.get_time() / 1000.0 

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

    def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()


