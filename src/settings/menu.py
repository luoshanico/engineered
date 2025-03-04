menu_map = {
    'main': {
        'active': True,
        'buttons': [
            {'action': 'nav', 'target': 'object', 'button': None, 'text': 'Add object', 'position': 0},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1},
        ],
        'inputs': []
    },
    'object': {
        'active': False,
        'buttons': [
            {'action': 'nav', 'target': 'ball', 'button': None, 'text': 'Ball', 'position': 0},
            {'action': 'nav', 'target': 'rectangle', 'button': None, 'text': 'Rectangle', 'position': 1},
            {'action': 'nav', 'target': 'ball', 'button': None, 'text': 'Triangle', 'position': 2},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3}
        ],
        'inputs': []
    },
    'constraint': {
        'active': False,
        'buttons': [
            {'action': 'nav', 'target': 'damped_spring', 'button': None, 'text': 'Add spring', 'position': 0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 1}
        ],
        'inputs': []
    },
    'ball': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Add ball', 'position': 0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 1}
        ],
        'inputs': [
            {'input':'mass', 'default value': 1,'entry': 'simple', 'position': 2},
            {'input':'radius', 'default value': 60,'entry': 'simple', 'position': 3},
            {'input':'elasticity', 'default value': 0.9,'entry': 'simple', 'position': 4},
            {'input':'friction', 'default value': 0.3,'entry': 'simple', 'position': 5},
            {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': 6}
        ]   
    },
    'damped_spring': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'damped_spring', 'button': None, 'text': 'Add Spring', 'position': 0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 1}
        ],
        'inputs': []
    }
}

button_locations = [
    (20, 40, 120, 30),
    (160, 40, 120, 30),
    (300, 40, 120, 30),
    (440, 40, 120, 30)
]

fontsizes = {
    'title':30,
    'header_1':20,
    'header_2':15,
    'text':10
}