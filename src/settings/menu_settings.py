menu_map = {
    'main': {
        'active': True,
        'buttons': [
            {'action': 'nav', 'target': 'object', 'button': None, 'text': 'Add object', 'position': 0, 'condition':0},
            # {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1, 'condition':0},
        ],
        'inputs': []
    },
    'object': {
        'active': False,
        'buttons': [
            {'action': 'nav', 'target': 'ball', 'button': None, 'text': 'Ball', 'position': 0, 'condition':0},
            {'action': 'nav', 'target': 'bar', 'button': None, 'text': 'Bar', 'position': 1, 'condition':0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3, 'condition':0}
        ],
        'inputs': []
    },
    'constraint': {
        'active': False,
        'buttons': [
            {'action': 'nav', 'target': 'damped_spring', 'button': None, 'text': 'Add spring', 'position': 0, 'condition':0},
            {'action': 'nav', 'target': 'pin_joint', 'button': None, 'text': 'Add pin joint', 'position': 1, 'condition':0},
            {'action': 'nav', 'target': 'pivot_joint', 'button': None, 'text': 'Add pivot joint', 'position': 2, 'condition':0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3, 'condition':0}
        ],
        'inputs': []
    },
    'ball': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Add ball', 'position': 0, 'condition':0},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1, 'condition':2},
            {'action': 'add', 'target': 'pin', 'button': None, 'text': 'Pin', 'position': 2, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 3, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 4, 'condition':0}
        ],
        'inputs': [
            {'input':'mass','default_value':1 ,'entry': 'simple', 'position': 0, 'input_field': None},
            {'input':'radius','default_value':60 ,'entry': 'simple', 'position': 1, 'input_field': None},
            {'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'position': 2, 'input_field': None},
            {'input':'friction','default_value':0.3,'entry': 'simple', 'position': 3, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': 4, 'input_field': None}
        ]   
    },
    'bar': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'bar', 'button': None, 'text': 'Add bar', 'position': 0, 'condition':0},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1, 'condition':2},
            {'action': 'add', 'target': 'pin', 'button': None, 'text': 'Pin', 'position': 2, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 3, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 4, 'condition':0}
        ],
        'inputs': [
            {'input':'mass','default_value':1 ,'entry': 'simple', 'position': 0, 'input_field': None},
            {'input':'length','default_value':100 ,'entry': 'simple', 'position': 1, 'input_field': None},
            {'input':'thickness','default_value':5 ,'entry': 'simple', 'position': 2, 'input_field': None},
            {'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'position': 3, 'input_field': None},
            {'input':'friction','default_value':0.3,'entry': 'simple', 'position': 4, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': 5, 'input_field': None}
        ]   
    },
    'damped_spring': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'damped_spring', 'button': None, 'text': 'add Spring', 'position': 0, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 1, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 2, 'condition':0}
        ],
        'inputs': [
            {'input':'rest length','default_value':10 ,'entry': 'simple', 'position': 0, 'input_field': None},
            {'input':'stiffness','default_value':10 ,'entry': 'simple', 'position': 1, 'input_field': None},
            {'input':'damping','default_value':0.3 ,'entry': 'simple', 'position': 2, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': 4, 'input_field': None}
        ]   
    },
    'pin_joint': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'pin_joint', 'button': None, 'text': 'Add pin joint', 'position': 0, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 1, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 2, 'condition':0}
        ],
        'inputs': []   
    },
    'pivot_joint': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'pivot_joint', 'button': None, 'text': 'Add pivot joint', 'position': 0, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 1, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 2, 'condition':0}
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

input_locations = [
    (20, 80, 120, 30),
    (160, 80, 120, 30),
    (300, 80, 120, 30),
    (440, 80, 120, 30),
    (580, 80, 120, 30)
]

fontsizes = {
    'title':30,
    'header_1':25,
    'header_2':20,
    'text':15
}