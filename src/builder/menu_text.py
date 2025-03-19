import pygame as pg
from settings import settings

class MenuText():
    def __init__(self, game, text):
        self.game = game
        self.text = text['text']

    def get_position(self,pos_idx):
        self.position = self.game.state_stack[-1].menu.menu_positions[pos_idx]

    def render(self):
        self.font_size = settings.fontsizes['header_1']
        self.font_color = settings.BLACK
        font = pg.font.Font(None, self.font_size)
        text = font.render(self.text, True, self.font_color)
        text_location = self.position
        self.game.surface.blit(text, text_location)
