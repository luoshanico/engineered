import pygame as pg
from settings import settings

class MenuText():
    def __init__(self, game, text):
        self.game = game
        self.text = text['text']
        self.font_size = settings.fontsizes['header_1']
        self.font_color = settings.BLACK
        self.text_position = (0,0,0,0)

    def get_position(self,pos_idx):
        self.item_position = self.game.state_stack[-1].menu.menu_positions[pos_idx]
        self.text_position = self.get_lower_left_aligned_position()

    def get_lower_left_aligned_position(self):
        font = pg.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, (255, 255, 255))
        _, text_height = text_surface.get_size()
        x = self.item_position[0]
        y = self.item_position[1] + self.item_position[3] - text_height
        return (x, y)

    def render(self):
        font = pg.font.Font(None, self.font_size)
        text = font.render(self.text, True, self.font_color)
        self.game.surface.blit(text, self.text_position)
