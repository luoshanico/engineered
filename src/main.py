import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
pymunk.pygame_util.positive_y_is_up = False
from settings import settings
from states.main_menu import Title
from assets import Assets

class Game():
    def __init__(self):
        pg.init()
        self.load_display()
        self.running, self.playing = True, True
        self.load_time()
        self.assets = Assets()
        self.load_states()

    def load_display(self):
        self.width, self.height = self.RES = settings.RES
        self.surface = pg.Surface(self.RES)
        self.screen = pg.display.set_mode(self.RES)

    def load_time(self):
        self.clock = pg.time.Clock()
        self.FPS = settings.FPS

    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)

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
        self.font = pg.font.Font(None, settings.fontsizes['title'])
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)

    def load_states(self):
        self.state_stack = []
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
        print(self.state_stack[-1])


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()


