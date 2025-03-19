import pygame as pg
from settings import general_settings
from settings import menu_settings

class MenuText():
    def __init__(self, game, text):
        self.game = game
        self.text = text['text']

    def get_position(self,pos_idx):
        self.position = menu_settings.menu_positions[pos_idx]

    def render(self):
        self.font_size = menu_settings.fontsizes['header_1']
        self.font_color = general_settings.BLACK
        font = pg.font.Font(None, self.font_size)
        text = font.render(self.text, True, self.font_color)
        text_location = self.position
        self.game.surface.blit(text, text_location)
