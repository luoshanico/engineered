menu_map = {
    'main': {
        'active': True,
        'items': [
            {'type':'button', 'action': 'nav', 'target': 'ball', 'object': None, 'text': 'Add ball', 'condition':0},
            {'type':'button', 'action': 'nav', 'target': 'bar', 'object': None, 'text': 'Add bar', 'condition':0},
            {'type':'button', 'action': 'delete_all_pins', 'target': None, 'object': None, 'text': 'Remove all pins', 'condition':3}
        ]
    },
    'constraint': {
        'active': False,
        'items': [
            {'type':'button', 'action': 'nav', 'target': 'damped_spring', 'object': None, 'text': 'Add spring', 'condition':0},
            {'type':'button', 'action': 'nav', 'target': 'pin_joint', 'object': None, 'text': 'Add pin joint', 'condition':0},
            {'type':'button', 'action': 'nav', 'target': 'pivot_joint', 'object': None, 'text': 'Add pivot joint', 'condition':0},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':None}
        ]
    },
    'ball': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit ball', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'add', 'target': 'ball', 'object': None, 'text': 'Add ball', 'condition':7},
            {'type':'input', 'input':'mass','default_value':1 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'radius','default_value':60 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'friction','default_value':0.3,'entry': 'simple', 'condition':0, 'object': None},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'bar', 'object': None, 'text': 'Add bar', 'condition':7},
            {'type':'button', 'action': 'add', 'target': 'ball', 'object': None, 'text': 'Add new ball', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'constraint', 'object': None, 'text': 'Add constraint', 'condition':2},
            {'type':'button', 'action': 'nav', 'target': 'motor', 'object': None, 'text': 'Add motor', 'condition':1},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'delete_constraints', 'target': None, 'object': None, 'text': 'Delete constraints', 'condition':4},
            {'type':'button', 'action': 'delete_selected_pins', 'target': None, 'object': None, 'text': 'Delete pins', 'condition':5},
            {'type':'button', 'action': 'delete_selected_motors', 'target': None, 'object': None, 'text': 'Delete motor', 'condition':6},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
            
        ]   
    },
    'bar': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit bar', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'nav', 'target': 'ball', 'object': None, 'text': 'Add ball', 'condition':7},
            {'type':'button', 'action': 'add', 'target': 'bar', 'object': None, 'text': 'Add bar', 'condition':7},
            {'type':'input', 'input':'mass','default_value':1 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'length','default_value':100 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'friction','default_value':0.3,'entry': 'simple', 'condition':0, 'object': None},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'add', 'target': 'bar', 'object': None, 'text': 'Add new bar', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'constraint', 'object': None, 'text': 'Add constraint', 'condition':2},
            {'type':'button', 'action': 'nav', 'target': 'motor', 'object': None, 'text': 'Add motor', 'condition':1},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'delete_constraints', 'target': None, 'object': None, 'text': 'Delete constraints', 'condition':4},
            {'type':'button', 'action': 'delete_selected_pins', 'target': None, 'object': None, 'text': 'Delete pins', 'condition':5},
            {'type':'button', 'action': 'delete_selected_motors', 'target': None, 'object': None, 'text': 'Delete motor', 'condition':6},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
        ]
    },
    'motor': {
        'active': False,
        'items': [
            {'type':'button', 'action': 'add', 'target': 'motor', 'object': None, 'text': 'Add motor', 'condition':1},
            {'type':'input', 'input':'rpm','default_value':100 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'max_force','default_value':50 ,'entry': 'simple', 'condition':0, 'object': None},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
            
        ]
    },
    'damped_spring': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit spring', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'add', 'target': 'damped_spring', 'object': None, 'text': 'add Spring', 'condition':2},
            {'type':'input', 'input':'rest length','default_value':10 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'stiffness','default_value':10 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'damping','default_value':0.3 ,'entry': 'simple', 'condition':0, 'object': None},
            
            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete', 'condition':1},

            {'type':'text', 'text':'', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
            
        ]
    },
    'pin_joint': {
        'active': False,
        'items': [
            {'type':'button', 'action': 'add', 'target': 'pin_joint', 'object': None, 'text': 'Add pin joint', 'condition':2},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
        ]
    },
    'pivot_joint': {
        'active': False,
        'items': [
            {'type':'button', 'action': 'add', 'target': 'pivot_joint', 'object': None, 'text': 'Add pivot joint', 'condition':2},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'main', 'object': None, 'text': 'Back', 'condition':0}
        ]
    }
}


