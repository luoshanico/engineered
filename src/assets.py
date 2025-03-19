import os
import pygame as pg


class Assets():
    def __init__(self):
        self.font_paths = {}
        self.icons = {}
        self.load_fonts()
        self.load_icons()

    def load_fonts(self):
        fonts_path = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts")
        for filename in os.listdir(fonts_path):
            if filename.lower().endswith((".ttf", ".otf")):
                full_path = os.path.join(fonts_path, filename)
                font_key = os.path.splitext(filename)[0]
                self.font_paths[font_key] = full_path
        print("Loaded fonts:", list(self.font_paths.keys()))

    def get_font(self, font_name, size):
        if font_name in self.font_paths:
            return pg.font.Font(self.font_paths[font_name], size)
        else:
            raise ValueError(f"Font '{font_name}' not found.")


    def load_icons(self):
        """Load all icons from the assets/icons folder."""
        icons_path = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
        for filename in os.listdir(icons_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                full_path = os.path.join(icons_path, filename)
                icon_key = os.path.splitext(filename)[0]
                self.icons[icon_key] = pg.image.load(full_path).convert_alpha()
        print("Loaded icons:", list(self.icons.keys()))