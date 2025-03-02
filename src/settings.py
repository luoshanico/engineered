

# Constants
RES = WIDTH, HEIGHT = 960, 540
MENUSIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
FPS = 60


# World
world = {
    'elasticity':0.8,
    'friction':0.2
    }

loading_bay = {
    'width':200,
    'height':150
}

# Collision categories
OBJECT_CAT = 1
WORLD_CAT = 2
MENU_CAT = 3

button_locations = [
    (20, 40, 120, 30),
    (160, 40, 120, 30),
    (300, 40, 120, 30),
    (440, 40, 120, 30)
]

# Default constraint values
DefaultConstraintValues = {
    'DampedSpring':(30, 5, 0.5),  # rest_length, stiffness, damping
    'PinJoint':None,
    'SlideJoint':(10,100)  # min, max
    }

fontsizes = {
    'title':30,
    'header_1':20,
    'header_2':15,
    'text':10
}