menu_map = {
    'main': {
        'active': True,
        'buttons': [
            {'action': 'nav', 'target': 'object', 'button': None, 'text': 'Add object', 'position': 0, 'condition':0},
            {'action': 'delete_all_pins', 'target': None, 'button': None, 'text': 'Remove all pins', 'position': 1, 'condition':3},
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
            {'action': 'nav', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': 2, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 3, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 4, 'condition':0},
            {'action': 'delete_constraints', 'target': None, 'button': None, 'text': 'Delete constraints', 'position': 5, 'condition':4},
            {'action': 'delete_selected_pins', 'target': None, 'button': None, 'text': 'Delete pins', 'position': 6, 'condition':5},
            {'action': 'delete_selected_motors', 'target': None, 'button': None, 'text': 'Delete motor', 'position': 7, 'condition':6}
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
            {'action': 'nav', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': 2, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 3, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 4, 'condition':0},
            {'action': 'delete_constraints', 'target': None, 'button': None, 'text': 'Delete constraints', 'position': 5, 'condition':4},
            {'action': 'delete_selected_pins', 'target': None, 'button': None, 'text': 'Delete pins', 'position': 6, 'condition':5},
            {'action': 'delete_selected_motors', 'target': None, 'button': None, 'text': 'Delete motor', 'position': 7, 'condition':6}
        ],
        'inputs': [
            {'input':'mass','default_value':1 ,'entry': 'simple', 'position': 0, 'input_field': None},
            {'input':'length','default_value':100 ,'entry': 'simple', 'position': 1, 'input_field': None},
            {'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'position': 2, 'input_field': None},
            {'input':'friction','default_value':0.3,'entry': 'simple', 'position': 3, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': 4, 'input_field': None}
        ]   
    },
    'motor': {
        'active': False,
        'buttons': [
            {'action': 'add', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': 0, 'condition':1},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': 1, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': 2, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3, 'condition':0},
            {'action': 'delete_constraints', 'target': None, 'button': None, 'text': 'Delete constraints', 'position': 4, 'condition':4},
            {'action': 'delete_selected_pins', 'target': None, 'button': None, 'text': 'Delete pins', 'position': 5, 'condition':5}
        ],
        'inputs': [
            {'input':'rpm','default_value':100 ,'entry': 'simple', 'position': 0, 'input_field': None},
            {'input':'max_force','default_value':50 ,'entry': 'simple', 'position': 1, 'input_field': None}
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
    (20, 40, 100, 30),
    (140, 40, 100, 30),
    (260, 40, 100, 30),
    (380, 40, 100, 30),
    (500, 40, 100, 30),
    (620, 40, 100, 30),
    (740, 40, 100, 30),
    (860, 40, 100, 30)

]

input_locations = [
    (20, 80, 100, 30),
    (140, 80, 100, 30),
    (260, 80, 100, 30),
    (380, 80, 100, 30),
    (500, 80, 100, 30)
]

fontsizes = {
    'title':30,
    'header_1':25,
    'header_2':20,
    'text':15
}