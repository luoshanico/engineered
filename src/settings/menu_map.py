menu_map = {
    'main': {
        'active': True,
        'items': [
            {'type':'text', 'text':'Add item', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'ball', 'object': None, 'text': 'Ball', 'icon':'object', 'condition':0},
            {'type':'button', 'action': 'nav', 'target': 'bar', 'object': None, 'text': 'Bar', 'icon':'object', 'condition':0},
            {'type':'button', 'action': 'delete_all_pins', 'target': None, 'object': None, 'text': 'Remove all pins', 'icon':'object', 'condition':3}
        ]
    },
    'constraint': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Add constraint', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'nav', 'target': 'damped_spring', 'object': None, 'text': 'Add spring', 'icon':'constraint',  'condition':0},
            {'type':'button', 'action': 'add', 'target': 'pin_joint', 'object': None, 'text': 'Add pin joint', 'icon':'constraint',  'condition':0},
            {'type':'button', 'action': 'add', 'target': 'pivot_joint', 'object': None, 'text': 'Add pivot joint', 'icon':'constraint',  'condition':0},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back',  'condition':None}
        ]
    },
    'ball': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit ball', 'object':None, 'condition': 1},
            {'type':'text', 'text':'Add item', 'object':None, 'condition': 7},
            {'type':'button', 'action': 'add', 'target': 'ball', 'object': None, 'text': 'Add ball', 'icon':'object', 'condition':7},
            {'type':'input', 'input':'mass','default_value':1 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'radius','default_value':60 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'friction','default_value':0.3,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'button', 'action': 'nav', 'target': 'bar', 'object': None, 'text': 'Add bar', 'icon':'object', 'condition':7},
            {'type':'button', 'action': 'add', 'target': 'ball', 'object': None, 'text': 'Add new ball', 'icon':'object', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'constraint', 'object': None, 'text': 'Add constraint', 'icon':'constraint', 'condition':2},
            {'type':'button', 'action': 'nav', 'target': 'motor', 'object': None, 'text': 'Add motor', 'icon':'motor', 'condition':1},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'delete_constraints', 'target': None, 'object': None, 'text': 'Delete constraints', 'icon':'constraint', 'condition':4},
            {'type':'button', 'action': 'delete_selected_pins', 'target': None, 'object': None, 'text': 'Delete pins', 'icon':'object', 'condition':5},
            {'type':'button', 'action': 'delete_selected_motors', 'target': None, 'object': None, 'text': 'Delete motor', 'icon':'motor', 'condition':6},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back',  'condition':0}
            
        ]   
    },
    'bar': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit bar', 'object':None, 'condition': 1},
            {'type':'text', 'text':'Add item', 'object':None, 'condition': 7},
            {'type':'button', 'action': 'nav', 'target': 'ball', 'object': None, 'text': 'Add ball', 'icon':'object', 'condition':7},
            {'type':'button', 'action': 'add', 'target': 'bar', 'object': None, 'text': 'Add bar', 'icon':'object', 'condition':7},
            {'type':'input', 'input':'mass','default_value':1 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'length','default_value':100 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'elasticity','default_value':0.9 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'friction','default_value':0.3,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'button', 'action': 'add', 'target': 'bar', 'object': None, 'text': 'Add new bar', 'icon':'object', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'constraint', 'object': None, 'text': 'Add constraint', 'icon':'constraint', 'condition':2},
            {'type':'button', 'action': 'nav', 'target': 'motor', 'object': None, 'text': 'Add motor', 'icon':'motor', 'condition':1},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'delete_constraints', 'target': None, 'object': None, 'text': 'Delete constraints', 'icon':'constraint', 'condition':4},
            {'type':'button', 'action': 'delete_selected_pins', 'target': None, 'object': None, 'text': 'Delete pins', 'icon':'object', 'condition':5},
            {'type':'button', 'action': 'delete_selected_motors', 'target': None, 'object': None, 'text': 'Delete motor', 'icon':'motor', 'condition':6},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back',  'condition':0}
        ]
    },
    'motor': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Add motor', 'object':None, 'condition': 0},
            {'type':'button', 'action': 'add', 'target': 'motor', 'object': None, 'text': 'Add motor', 'icon':'motor', 'condition':1},
            {'type':'input', 'input':'rpm','default_value':100 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'max_force','default_value':50 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back', 'condition':0}
            
        ]
    },
    'damped_spring': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit spring', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'add', 'target': 'damped_spring', 'object': None, 'text': 'Add spring', 'icon':'constraint', 'condition':2},
            {'type':'input', 'input':'rest length','default_value':100 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'stiffness','default_value':10 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'input', 'input':'damping','default_value':0.3 ,'entry': 'simple', 'condition':0, 'object': None},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'nav', 'target': 'constraint', 'object': None, 'text': 'Back', 'icon':'back', 'condition':2},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back', 'condition':8}   
        ]
    },
    'pin_joint': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit pin joint', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back', 'condition':0}   
        ]
    },
    'pivot_joint': {
        'active': False,
        'items': [
            {'type':'text', 'text':'Edit pivot joint', 'object':None, 'condition': 1},
            {'type':'button', 'action': 'delete', 'target': None, 'object': None, 'text': 'Delete selected', 'condition':1},
            {'type':'button', 'action': 'back', 'target': 'main', 'object': None, 'text': 'Back', 'icon':'back', 'condition':0}   
        ]
    }
}


