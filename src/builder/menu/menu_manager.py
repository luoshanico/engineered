

class MenuManager:
    def __init__(self, game):
        self.game = game
        self.menu_needs_update = True  # Flag indicating the menu needs recalculation

    def mark_dirty(self):
        self.menu_needs_update = True

    def recalc_if_needed(self):
        if self.menu_needs_update:
            self.game.state_stack[-1].menu.calculate_menu_positions()
            self.menu_needs_update = False