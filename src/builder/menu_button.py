import pygame as pg
from settings import general_settings
from settings import menu_settings

class Button():
    def __init__(self,game,btn_data):
        self.data = btn_data
        self.action = btn_data['action']
        self.target = btn_data['target']
        self.text = btn_data['text']
        self.game = game
        self.menu = game.state_stack[-1].menu

    def get_position(self,position):
        self.position = position
    
    def render(self):
        self.get_button_render_inputs()
        self.add_button(self.game.surface)

    def get_button_render_inputs(self):
        self.location = menu_settings.menu_locations[self.position]
        self.radius = menu_settings.button_radius
        self.color = self.get_button_color()
        self.font_size = menu_settings.fontsizes['header_2']
        self.font_color = general_settings.WHITE

    def get_button_color(self): 
        if 'delete' in self.action:
            return general_settings.RED
        if self.target != 'main':
            return general_settings.BLUE
        else:
            return general_settings.BLACK
    
    def add_button(self, surface):
        self.shape = pg.draw.rect(surface, self.color, self.location, border_radius=self.radius)
        font = pg.font.Font(None, self.font_size)
        button_text = font.render(self.text, True, self.font_color)
        text_location = self.center_text_in_rectangle(self.text)
        surface.blit(button_text, text_location)
    
    def center_text_in_rectangle(self):
        font = pg.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()
        x = self.location[0] + (self.location[2] - text_width) // 2
        y = self.location[1] + (self.location[3] - text_height) // 2
        return (x, y)