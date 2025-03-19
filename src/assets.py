import os
import pygame as pg


class Assets():
    def __init__(self):
        self.fonts = {}
        self.icons = {}
        self.load_fonts()
        self.load_icons()

    def load_fonts(self):
        """Load all fonts from the assets/fonts folder."""
        fonts_path = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts")
        for filename in os.listdir(fonts_path):
            if filename.lower().endswith((".ttf", ".otf")):
                full_path = os.path.join(fonts_path, filename)
                font_key = os.path.splitext(filename)[0]
                self.fonts[font_key] = pg.font.Font(full_path, 24)
        print("Loaded fonts:", list(self.fonts.keys()))
    
    def load_icons(self):
        """Load all icons from the assets/icons folder."""
        icons_path = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
        for filename in os.listdir(icons_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                full_path = os.path.join(icons_path, filename)
                icon_key = os.path.splitext(filename)[0]
                self.icons[icon_key] = pg.image.load(full_path).convert_alpha()
        print("Loaded icons:", list(self.icons.keys()))