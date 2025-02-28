

# Constants
RES = WIDTH, HEIGHT = 960, 540
MENUSIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60


# World
world = {
    'elasticity':0.8,
    'friction':0.2
    }

# Collision categories
OBJECT_CAT = 1
WORLD_CAT = 2
MENU_CAT = 3



# Default constraint values
DefaultConstraintValues = {
    'DampedSpring':(30, 5, 0.5),  # rest_length, stiffness, damping
    'PinJoint':None,
    'SlideJoint':(10,100)  # min, max
    }

fontsizes = {
    'title':30,
    'header_1':25,
    'header_2':20,
    'text':15,
}