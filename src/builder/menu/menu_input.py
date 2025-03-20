import pygame as pg
from settings import settings

class InputField:
    def __init__(self, game, menu_item):
        self.game = game
        self.get_display_strings(menu_item)
        self.get_formats()
        self.selected = False
        self.text_highlighted = False
        self.active = True

    def get_position(self,pos_idx):
        self.position = self.game.state_stack[-1].menu.menu_positions[pos_idx]
        self.get_input_field_rectangles()

    def get_input_field_rectangles(self):
        self.border_rect = pg.Rect(self.position)
        self.value_rect_dims = self.get_value_rect_dims()
        self.value_rect = pg.Rect(self.value_rect_dims)

    def get_value_rect_dims(self):
        x_pos, y_pos, width, height = self.border_rect
        self.value_rect_radius = settings.menu_dims['input_value_radius']
        x_scaler = 0.9
        y_scaler = 0.8
        return (x_pos + width * (1/2), y_pos + (height * (1 - y_scaler))/2 , width * (1/2) * x_scaler, height * y_scaler)

    def get_display_strings(self, menu_item):
        self.input_name = str(menu_item['input'])
        self.value = str(menu_item['default_value'])
    
    def get_formats(self):
        self.input_name_font_size = settings.fontsizes['input_name']
        self.input_name_font = self.game.assets.get_font('Roobert-Regular',self.input_name_font_size)
        self.value_font_size = settings.fontsizes['input_value']
        self.value_font = self.game.assets.get_font('Roobert-Medium',self.value_font_size)
        self.input_name_color = settings.GREY
        self.value_color = settings.GREEN
        self.bg_color = settings.DARK_BLUE
        self.border_color = settings.GREEN

    def render(self):
        self.draw_input_name()
        self.draw_value_rectangle()
        self.draw_value()        
        
    def draw_input_name(self):
        input_name_surface = self.input_name_font.render(self.input_name, True, self.input_name_color)
        text_location = self.align_left_middle_text_in_rectangle(
            self.border_rect,
            self.input_name_font,
            self.input_name,
            5)
        self.game.surface.blit(input_name_surface, text_location)

    def align_left_middle_text_in_rectangle(self, rectangle_dims, font, text, left_margin):
        text_surface = font.render(text, True, settings.WHITE)
        _, text_height = text_surface.get_size()
        x = rectangle_dims[0] + left_margin
        y = rectangle_dims[1] + (rectangle_dims[3] - text_height) // 2
        return (x, y)
    
    def center_text_in_rectangle(self,text,font,rect):
        text_surface = font.render(text, True, settings.WHITE)
        text_width, text_height = text_surface.get_size()
        x = rect[0] + (rect[2] - text_width) // 2
        y = rect[1] + (rect[3] - text_height) // 2
        return (x, y)

    def draw_value_rectangle(self):
        pg.draw.rect(self.game.surface, self.bg_color, self.value_rect, border_radius=self.value_rect_radius)
        border_color = self.border_color if not self.selected else (0, 255, 0)
        pg.draw.rect(self.game.surface, border_color, self.value_rect, width=2, border_radius=self.value_rect_radius)

    def draw_value(self):
        value_surface = self.value_font.render(self.value, True, self.value_color)
        text_location = self.center_text_in_rectangle(
            self.value,
            self.value_font,
            self.value_rect,
            )
        self.game.surface.blit(value_surface, text_location)

    def get_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Toggle active state if the user clicks inside the input field.
            if self.value_rect.collidepoint(event.pos):
                self.selected = True
                self.text_highlighted = True  # Mark the text as selected (highlighted)
            else:
                self.selected = False
        if event.type == pg.KEYDOWN and self.selected:
            # If the text is "highlighted", clear it on first key press.
            if self.text_highlighted:
                self.value = ""
                self.text_highlighted = False
            if event.key == pg.K_BACKSPACE:
                self.value = self.value[:-1]
            elif event.key in (pg.K_RETURN, pg.K_KP_ENTER):
                self.selected = False
                self.game.state_stack[-1].manager.apply_updated_attributes_to_selected_components()
            else:
                # Optionally, filter input so only numbers (and one decimal) are accepted.
                if event.unicode.isdigit() or (event.unicode == '.' and '.' not in self.value):
                    self.value += event.unicode
            

    def update(self):
        pass

    

