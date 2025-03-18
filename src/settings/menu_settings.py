import settings.general_settings

menu_map = {
    'main': {
        'active': True,
        'text': [],
        'buttons': [
            {'action': 'nav', 'target': 'ball', 'button': None, 'text': 'Add ball', 'position': None, 'condition':0},
            {'action': 'nav', 'target': 'bar', 'button': None, 'text': 'Add bar', 'position': None, 'condition':0},
            {'action': 'delete_all_pins', 'target': None, 'button': None, 'text': 'Remove all pins', 'position': 2, 'condition':3}
        ],
        'inputs': []
    },
    'constraint': {
        'active': False,
        'text': [],
        'buttons': [
            {'action': 'nav', 'target': 'damped_spring', 'button': None, 'text': 'Add spring', 'position': None, 'condition':0},
            {'action': 'nav', 'target': 'pin_joint', 'button': None, 'text': 'Add pin joint', 'position': None, 'condition':0},
            {'action': 'nav', 'target': 'pivot_joint', 'button': None, 'text': 'Add pivot joint', 'position': None, 'condition':0},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': 3, 'condition':None}
        ],
        'inputs': []
    },
    'ball': {
        'active': False,
        'text' : [{'text':'Edit ball', 'position':0, 'condition': 1}],
        'buttons': [
            {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Add ball', 'position': None, 'condition':7},  
            {'action': 'nav', 'target': 'bar', 'button': None, 'text': 'Add bar', 'position': None, 'condition':7},
            {'action': 'add', 'target': 'ball', 'button': None, 'text': 'Add new ball', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': None, 'condition':2},
            {'action': 'nav', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': None, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete selected', 'position': None, 'condition':1},
            {'action': 'delete_constraints', 'target': None, 'button': None, 'text': 'Delete constraints', 'position': None, 'condition':4},
            {'action': 'delete_selected_pins', 'target': None, 'button': None, 'text': 'Delete pins', 'position': None, 'condition':5},
            {'action': 'delete_selected_motors', 'target': None, 'button': None, 'text': 'Delete motor', 'position': None, 'condition':6},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': [
            {'input':'mass','default_value':1 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'radius','default_value':60 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'friction','default_value':0.3,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': None, 'input_field': None}
        ]   
    },
    'bar': {
        'active': False,
        'text' : [{'text':'Edit ball', 'position':0, 'condition': 1}],
        'buttons': [
            {'action': 'nav', 'target': 'ball', 'button': None, 'text': 'Add ball', 'position': None, 'condition':7},
            {'action': 'add', 'target': 'bar', 'button': None, 'text': 'Add bar', 'position': None, 'condition':7},
            {'action': 'add', 'target': 'bar', 'button': None, 'text': 'Add new bar', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': None, 'condition':2},
            {'action': 'nav', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': None, 'condition':1},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete selected', 'position': None, 'condition':1},
            {'action': 'delete_constraints', 'target': None, 'button': None, 'text': 'Delete constraints', 'position': None, 'condition':4},
            {'action': 'delete_selected_pins', 'target': None, 'button': None, 'text': 'Delete pins', 'position': None, 'condition':5},
            {'action': 'delete_selected_motors', 'target': None, 'button': None, 'text': 'Delete motor', 'position': None, 'condition':6},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': [
            {'input':'mass','default_value':1 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'length','default_value':100 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'friction','default_value':0.3,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': None, 'input_field': None}
        ]   
    },
    'motor': {
        'active': False,
        'text': [],
        'buttons': [
            {'action': 'add', 'target': 'motor', 'button': None, 'text': 'Add motor', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'constraint', 'button': None, 'text': 'Add constraint', 'position': None, 'condition':2},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': [
            {'input':'rpm','default_value':100 ,'entry': 'simple', 'position': None, 'input_field': None},
            {'input':'max_force','default_value':50 ,'entry': 'simple', 'position': None, 'input_field': None}
        ]   
    },
    'damped_spring': {
        'active': False,
        'text': [],
        'buttons': [
            {'action': 'add', 'target': 'damped_spring', 'button': None, 'text': 'add Spring', 'position': None, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': [
            {'input':'rest length','default_value':10 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'stiffness','default_value':10 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None},
            {'input':'damping','default_value':0.3 ,'entry': 'simple', 'position': None, 'condition':0, 'input_field': None}
            # {'input':'colour', 'default value': 'Black','entry': 'dropdown', 'position': None, 'input_field': None}
        ]   
    },
    'pin_joint': {
        'active': False,
        'text': [],
        'buttons': [
            {'action': 'add', 'target': 'pin_joint', 'button': None, 'text': 'Add pin joint', 'position': None, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': []   
    },
    'pivot_joint': {
        'active': False,
        'text': [],
        'buttons': [
            {'action': 'add', 'target': 'pivot_joint', 'button': None, 'text': 'Add pivot joint', 'position': None, 'condition':2},
            {'action': 'delete', 'target': None, 'button': None, 'text': 'Delete', 'position': None, 'condition':1},
            {'action': 'nav', 'target': 'main', 'button': None, 'text': 'Back', 'position': None, 'condition':0}
        ],
        'inputs': []   
    }
}

button_radius = 5
button_width = 100
button_height = 30
button_start_x = 20
button_start_y = 100
button_gap = 20
max_buttons = (settings.general_settings.HEIGHT - button_start_y) // (button_height + button_gap)

menu_locations = [(button_start_x, button_start_y + i * (button_height + button_gap), button_width, button_height) for i in range(max_buttons)]


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

