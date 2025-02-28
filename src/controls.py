import pymunk.pygame_util
import pygame as pg
from pygame.locals import *
pymunk.pygame_util.positive_y_is_up = False
from random import randrange
import settings, states.menu as menu


def mouseleftclick(space, menu_area):
    mouse_pos = pg.mouse.get_pos()

    if menu.object_button.collidepoint(mouse_pos):
        print("Add object...")
    elif menu.constraint_button.collidepoint(mouse_pos):
        print("Add constraint...")
    
    # hit = space.point_query(mouse_pos, max_distance=10, shape_filter=[])

    # if not hit:  # if mouse is in menu area or blank space or world, do nothing
        
    #     # If button then call that button's function. 
    #     if hit[0].shape in menu_area:



        
        # # If nothing is selected yet, select the first object
        # if selected_object_1 is None:
        #     selected_object_1 = hit[0].shape
            
        #     print(f"Object 1 selected: {selected_object_1}")
        # # Otherwise, select the second object
        # elif selected_object_2 is None:
        #     selected_object_2 = hit[0].shape
        #     print(f"Object 2 selected: {selected_object_2}")
        
        # # Link objects
        # if selected_object_1 and selected_object_2:
        #     print(f"Link object: {selected_object_1} to object: {selected_object_2}")
        #     add_constraint(constraint_type, selected_object_1.body,selected_object_2.body)
            
        #     # Reset the selection
        #     selected_object_1 = None
        #     selected_object_2 = None





    
    
    # if mouse is on button, then click the button.

    # if on game object then
        # if in "moving" state, then we have select functionality, plus drag and move and drop functionality. 

        # if in create_object state, then create specified object where I click

        # if in constraint state, then select object1, select object2 adds constraint


