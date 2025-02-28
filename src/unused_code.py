# def create_ball(space,pos):
#         ball_mass, ball_radius = 1, 60
#         ball_moment = pymunk.moment_for_circle(ball_mass, 0 ,ball_radius)
#         ball_body = pymunk.Body(ball_mass, ball_moment)
#         ball_body.position = pos
#         ball_shape = pymunk.Circle(ball_body, ball_radius)
#         ball_shape.elasticity = 0.8
#         ball_shape.friction = 0.5
#         ball_shape.collision_type = settings.OBJECT_CAT
#         space.add(ball_body, ball_shape)
#         return ball_body, ball_shape

#     # Create two balls
#     b1_body, b1_shape = create_ball(space,pos=(settings.WIDTH // 2 - 100,600))
#     b2_body, b2_shape  = create_ball(space,pos=(settings.WIDTH // 2 + 100,600))
    
    
#     def add_constraint(constraint_type, body1, body2):
#         if body1 is None or body2 is None:
#             print("Error: One or both bodies are None!")
#             return
        
#         print("selected_object_1: ",type(body1), body1)
#         print("selected_object_2: ",type(body2), body2)
        
#         if constraint_type == 'damped_spring':
#             try:
#                 c = pymunk.DampedSpring(body1, body2, (60, 0), (-60, 0), 20, 5, 0.3)
#                 space.add(c)
#             except AssertionError:
#                 pass
        
#         if constraint_type == 'damped_spring':
#             try:
#                 c = pymunk.DampedSpring(body1, body2, (60, 0), (-60, 0), 20, 5, 0.3)
#                 space.add(c)
#             except AssertionError:
#                 pass


    
#     # Global variables for selected objects
#     selected_object_1 = None
#     selected_object_2 = None
#     constraint_type = 'damped_spring'
#     rest_length, stiffness, damping = 50.0, 5.0, 0.3  # Default constraint values


          # mouse_pos = pg.mouse.get_pos()

                    # # Use Pymunk's point_query to check if the mouse is over any object
                    # hit = space.point_query(mouse_pos, max_distance=10, shape_filter=[])
                    # if hit:
                    #     # If nothing is selected yet, select the first object
                    #     if selected_object_1 is None:
                    #         selected_object_1 = hit[0].shape
                            
                    #         print(f"Object 1 selected: {selected_object_1}")
                    #     # Otherwise, select the second object
                    #     elif selected_object_2 is None:
                    #         selected_object_2 = hit[0].shape
                    #         print(f"Object 2 selected: {selected_object_2}")
                        
                    #     # Link objects
                    #     if selected_object_1 and selected_object_2:
                    #         print(f"Link object: {selected_object_1} to object: {selected_object_2}")
                    #         add_constraint(constraint_type, selected_object_1.body,selected_object_2.body)
                            
                    #         # Reset the selection
                    #         selected_object_1 = None
                    #         selected_object_2 = None



# def main():    

#     running = True
#     while running:
#         surface.fill(pg.Color('black'))

#         # Draw Engineer Menu
#         menu_area = menu.draw_engineer_menu(screen)

#         for i in pg.event.get():
#             if i.type == pg.QUIT:
#                 running = False
            
          

#         # Draw the objects
#         for shape in space.shapes:
#             if isinstance(shape, pymunk.Circle):
#                 color = settings.RED if shape.body == selected_object_1 else settings.GREEN if shape.body == selected_object_2 else settings.BLUE
#                 pg.draw.circle(screen, color, (int(shape.body.position.x), int(shape.body.position.y)), int(shape.radius))


#         space.step(1 / settings.FPS)
#         space.debug_draw(draw_options)

#         pg.display.flip()
#         clock.tick(settings.FPS)

#     pg.quit()