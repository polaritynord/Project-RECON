import engine
from raylib import *
from pyray import Vector2

class TextLabel:
    def __init__(self, parent, text, pos, font, visible, size, spacing, color):
        self.parent = parent
        self.text = text
        self.pos = pos
        self.font = font
        self.visible = visible
        self.size = size
        self.spacing = spacing
        self.color = color
    
    def engineRender(self, offset):
        font_dat = engine.assets.getFont(self.font)
        size = self.size if self.size > 0 else font_dat.baseSize
        # Set position (offseted by both canvas & node)
        new_pos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)

        DrawTextEx(font_dat, self.text.encode(), new_pos, size, self.spacing, self.color)
