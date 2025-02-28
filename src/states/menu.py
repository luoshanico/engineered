# UI for Engineer Menu
import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
pymunk.pygame_util.positive_y_is_up = False
from random import randrange
import settings
import utils
from state import State




def draw_engineer_menu(screen):
    menu_area = pg.draw.rect(screen, settings.WHITE, (0, 0, settings.WIDTH, settings.MENUSIZE))  # Menu background
    pg.draw.rect(screen, settings.BLACK, (0, 0, settings.WIDTH, settings.MENUSIZE), 3)  # Menu border
    return menu_area
    

def main_menu(screen):
    # Title
    title_font = pg.font.Font(None, settings.fontsizes['title'])
    text = title_font.render("Engineer Menu", True, settings.BLACK)
    screen.blit(text, (10, 10))

    # Add object button
    location = (150, 40, 140, 30)
    color = settings.BLUE
    text = "Add Object"
    font_size = settings.fontsizes['header_1']
    font_color = settings.WHITE
    object_button = utils.add_button(screen, location, color, text, font_size, font_color)

    # Add constraint Button
    location = (320, 40, 140, 30)
    color = settings.BLUE
    text = "Add Constraint"
    font_size = settings.fontsizes['header_1']
    font_color = settings.WHITE
    constraint_button = utils.add_button(screen, location, color, text, font_size, font_color)

    return object_button, constraint_button

    
def constraint_menu(screen):
    # Title
    title_font = pg.font.Font(None, settings.fontsizes['title'])
    text = title_font.render("Select constraint type", True, settings.BLACK)
    screen.blit(text, (10, 10))

    # Damped Spring
    location = (100, 40, 100, 30)
    color = settings.BLUE
    text = "Damped Spring"
    font_size = settings.fontsizes['header_2']
    font_color = settings.WHITE
    damped_spring_button = utils.add_button(screen, location, color, text, font_size, font_color)

    # Pin Joint
    location = (220, 40, 100, 30)
    color = settings.BLUE
    text = "Pin Joint"
    font_size = settings.fontsizes['header_2']
    font_color = settings.WHITE
    pin_joint_button = utils.add_button(screen, location, color, text, font_size, font_color)

    # Slide Joint
    location = (340, 40, 100, 30)
    color = settings.BLUE
    text = "Pin Joint"
    font_size = settings.fontsizes['header_2']
    font_color = settings.WHITE
    slide_joint_button = utils.add_button(screen, location, color, text, font_size, font_color)

    return damped_spring_button, pin_joint_button, slide_joint_button
    

def damped_spring_menu(screen):
    # Title
    title_font = pg.font.Font(None, settings.fontsizes['title'])
    text = title_font.render("Add Damped Spring", True, settings.BLACK)
    screen.blit(text, (10, 10))







