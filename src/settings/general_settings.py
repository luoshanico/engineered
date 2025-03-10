# Game constants
RES = WIDTH, HEIGHT = 960, 540
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


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)


default_object_settings = {
    'ball':{
        'mass':1, 'radius':60, 'elasticity':0.9, 'friction':0.3
    },
    'rectangle':{
        'mass':1
    }
}