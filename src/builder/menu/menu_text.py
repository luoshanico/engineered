import pygame as pg
from settings import settings

class MenuText():
    def __init__(self, game, text):
        self.game = game
        self.text = text['text']
        self.font_size = settings.fontsizes['text']
        self.font_color = settings.BLACK
        self.text_position = (0,0,0,0)
        self.active = True

    def get_position(self,pos_idx):
        self.item_position = self.game.state_stack[-1].menu.menu_positions[pos_idx]
        self.text_position = self.get_lower_centre_aligned_position()

    def get_lower_left_aligned_position(self):
        font = self.game.assets.get_font('Roobert-Bold',self.font_size)
        text_surface = font.render(self.text, True, settings.WHITE)
        _, text_height = text_surface.get_size()
        x = self.item_position[0]
        y = self.item_position[1] + self.item_position[3] - text_height
        return (x, y)
    
    def get_centre_middle_aligned_position(self):
        font = self.game.assets.get_font('Roobert-Bold',self.font_size)
        text_surface = font.render(self.text, True, settings.WHITE)
        text_width, text_height = text_surface.get_size()
        x = self.item_position[0] + (self.item_position[2] - text_width) // 2
        y = self.item_position[1] + (self.item_position[3] - text_height) // 2
        return (x, y)
    
    def get_lower_centre_aligned_position(self):
        font = self.game.assets.get_font('Roobert-Bold',self.font_size)
        text_surface = font.render(self.text, True, settings.WHITE)
        text_width, text_height = text_surface.get_size()
        x = self.item_position[0] + (self.item_position[2] - text_width) // 2
        y = self.item_position[1] + self.item_position[3] - text_height
        return (x, y)

    def render(self):
        font = self.game.assets.get_font('Roobert-Bold',self.font_size)
        text = font.render(self.text, True, self.font_color)
        self.game.surface.blit(text, self.text_position)
