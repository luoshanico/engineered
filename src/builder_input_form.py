import pygame as pg
from settings import general
from settings import menu

class InputField:
    def __init__(self, border_rect_dims, input_name="", default_value=""):
        self.get_input_field_rectangles(border_rect_dims)
        self.get_display_strings(input_name, default_value)
        self.get_formats()
        self.active = False


    def get_input_field_rectangles(self,border_rect_dims):
        self.border_rect = pg.Rect(border_rect_dims)
        self.value_rect_dims = self.get_value_rect_dims(border_rect_dims)
        self.value_rect = pg.Rect(self.value_rect_dims)

    def get_value_rect_dims(self, border_rect):
        x_pos, y_pos, width, height = border_rect
        return (x_pos + width * (3/4), y_pos , width * (1/4), height)

    def get_display_strings(self,input_name="", default_value=""):
        self.input_name = str(input_name)
        self.value = str(default_value)
    
    def get_formats(self):
        self.input_name_font_size = menu.fontsizes['text']
        self.input_name_font = pg.font.Font(None, self.input_name_font_size)
        self.value_font_size = menu.fontsizes['text']
        self.value_font = pg.font.Font(None, self.value_font_size)
        self.input_name_color = general.BLACK
        self.value_color = general.BLACK
        self.bg_color = general.WHITE
        self.border_color = general.BLACK

    def draw(self, surface):
        self.draw_input_name(surface)
        self.draw_value_rectangle(surface)
        self.draw_value(surface)
        

    def draw_input_name(self,surface):
        input_name_surface = self.font.render(self.input_name, True, self.input_name_color)
        text_location = self.align_left_middle_text_in_rectangle(
            self.border_rect_dims,
            self.input_name_font_size,
            self.input_name,
            5)
        surface.blit(input_name_surface, text_location)

    def align_left_middle_text_in_rectangle(self, rectangle_dims, font_size, text, left_margin):
        font = pg.font.Font(None, font_size)
        text_surface = font.render(text, True, (255, 255, 255))
        _, text_height = text_surface.get_size()
        x = rectangle_dims[0] + left_margin
        y = rectangle_dims[1] + (rectangle_dims[3] - text_height) // 2
        return (x, y)

    def draw_value_rectangle(self, surface):
        pg.draw.rect(surface, self.bg_color, self.value_rect)
        border_color = self.border_color if not self.active else (0, 255, 0)
        pg.draw.rect(surface, border_color, self.value_rect, 2)

    def draw_value(self, surface):
        value_surface = self.font.render(self.value, True, self.value_color)
        surface.blit(value_surface, (self.value_rect.x + 5, self.value_rect.y + 5))

    
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Toggle active state if the user clicks inside the input field.
            if self.value_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_BACKSPACE:
                self.value = self.value[:-1]
            elif event.key in (pg.K_RETURN, pg.K_KP_ENTER):
                # You might decide to deactivate on enter, if desired.
                self.active = False
            else:
                # Optionally, filter input so only numbers are accepted:
                if event.unicode.isdigit() or (event.unicode == '.' and '.' not in self.value):
                    self.value += event.unicode
            

    def update(self):
        pass

    def render(self, surface):
        self.draw(surface)

