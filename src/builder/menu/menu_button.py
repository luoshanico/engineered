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
        self.get_icon()
        self.active = True
        
    def get_position(self,pos_idx):
        self.position = self.game.state_stack[-1].menu.menu_positions[pos_idx]
    
    def render(self):
        self.get_button_render_inputs()
        self.render_button_shape()
        self.render_icon()
        self.render_button_text()

    def get_button_render_inputs(self):
        self.radius = settings.menu_dims['button_radius']
        self.color = self.get_button_color()
        self.font_size = settings.fontsizes['button']
        self.font_color = settings.DARK_BLUE

    def get_button_color(self): 
        if 'delete' in self.action:
            return settings.PINK
        if self.text in ['Back','Controls']:
            return settings.GREY
        else:
            return settings.GREEN
    
    def render_button_shape(self):
        self.shape = pg.draw.rect(self.game.surface, self.color, self.position, border_radius=self.radius)

    def get_icon(self):
        self.icon_offset = 0
        self.icon_left_margin = 10
        if 'icon' in self.data and self.data['icon']:
            # Look up the icon using its key.
            self.icon = self.game.assets.icons.get(self.data['icon'])
        else:
            self.icon = None
            

    def get_icon_target_height(self):
        self.icon_button_ratio = 0.7
        self.icon_target_height = int(self.position[3] * self.icon_button_ratio)

    def render_icon(self):
        if self.icon and self.position != (0,0,0,0):
            self.get_icon_target_height()
            self.icon = self.scale_icon()
            self.icon_pos = self.get_icon_position()
            self.game.surface.blit(self.icon, self.icon_pos)
            self.icon_offset = int(self.icon.get_rect().width) + self.icon_left_margin
        else:
            self.icon_offset = 0

    def get_icon_position(self):
        icon_x = self.position[0] + self.icon_left_margin
        icon_y = self.position[1] + (self.position[3] - self.icon_target_height) // 2
        return (icon_x,icon_y)
    
    def scale_icon(self):
        icon_rect = self.icon.get_rect()
        scale_factor = self.icon_target_height / icon_rect.height
        new_width = int(icon_rect.width * scale_factor)
        scaled_icon_surface = pg.transform.smoothscale(self.icon, (new_width, self.icon_target_height))
        return scaled_icon_surface
    
    def render_button_text(self):
        self.font = self.game.assets.get_font('Roobert-SemiBold', self.font_size)
        button_text = self.font.render(self.text, True, self.font_color)
        text_location = self.left_middle_text_in_rectangle(settings.menu_dims['button_text_left_margin'])
        self.game.surface.blit(button_text, text_location)
    
    def left_middle_text_in_rectangle(self, left_margin):
        text_surface = self.font.render(self.text, True, settings.WHITE)
        _, text_height = text_surface.get_size()
        x = self.position[0] + left_margin + self.icon_offset
        y = self.position[1] + (self.position[3] - text_height) // 2
        return (x, y)