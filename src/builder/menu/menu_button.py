import pygame as pg
from settings import settings

class Button():
    def __init__(self,game,btn_data):
        self.game = game
        self.data = btn_data
        self.action = btn_data['action']
        self.target = btn_data['target']
        self.text = btn_data['text']
        self.position = (0,0,0,0)
        self.shape = None
        self.active = True
        
    def get_position(self,pos_idx):
        self.position = self.game.state_stack[-1].menu.menu_positions[pos_idx]
    
    def render(self):
        self.get_button_render_inputs()
        self.render_button(self.game.surface)

    def get_button_render_inputs(self):
        self.radius = settings.menu_dims['button_radius']
        self.color = self.get_button_color()
        self.font_size = settings.fontsizes['header_2']
        self.font_color = settings.WHITE

    def get_button_color(self): 
        if 'delete' in self.action:
            return settings.RED
        elif self.target != 'main':
            return settings.BLUE
        else:
            return settings.BLACK
    
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