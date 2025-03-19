import pygame as pg
from settings import general_settings
from settings import menu_settings

class Button():
    def __init__(self,game,btn_data):
        self.data = btn_data
        self.action = btn_data['action']
        self.target = btn_data['target']
        self.text = btn_data['text']
        self.get_position(0)
        self.shape = None
        self.game = game

    def get_position(self,pos_idx):
        self.position = menu_settings.menu_positions[pos_idx]
    
    def render(self):
        self.get_button_render_inputs()
        self.render_button(self.game.surface)

    def get_button_render_inputs(self):
        self.radius = menu_settings.button_radius
        self.color = self.get_button_color()
        self.font_size = menu_settings.fontsizes['header_2']
        self.font_color = general_settings.WHITE

    def get_button_color(self): 
        if 'delete' in self.action:
            return general_settings.RED
        elif self.target != 'main':
            return general_settings.BLUE
        else:
            return general_settings.BLACK
    
    def render_button(self, surface):
        self.shape = pg.draw.rect(surface, self.color, self.position, border_radius=self.radius)
        font = pg.font.Font(None, self.font_size)
        button_text = font.render(self.text, True, self.font_color)
        text_location = self.center_text_in_rectangle()
        surface.blit(button_text, text_location)
    
    def center_text_in_rectangle(self):
        font = pg.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()
        x = self.position[0] + (self.position[2] - text_width) // 2
        y = self.position[1] + (self.position[3] - text_height) // 2
        return (x, y)