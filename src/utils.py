import pygame as pg

def add_button(screen, location, color, text, font_size, font_color):    
    button_rect = pg.draw.rect(screen, color, location)
    font = pg.font.Font(None, font_size)
    button_text = font.render(text, True, font_color)
    text_location = center_text_in_rectangle(location, font_size, text)
    screen.blit(button_text, text_location)
    
    return button_rect


def center_text_in_rectangle(rectangle_dims, font_size, text):
    
    # Create a font object
    font = pg.font.Font(None, font_size)  # You can replace None with a path to a specific font if desired
    
    # Render the text (get a surface with the text rendered)
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    
    # Get the dimensions of the text
    text_width, text_height = text_surface.get_size()
    
    # Calculate the position to center the text in the rectangle
    x = rectangle_dims[0] + (rectangle_dims[2] - text_width) // 2
    y = rectangle_dims[1] + (rectangle_dims[3] - text_height) // 2
    
    return (x, y)
