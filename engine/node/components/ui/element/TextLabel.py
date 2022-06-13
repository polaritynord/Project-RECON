import engine
from raylib import *
from pyray import Vector2

class TextLabel:
    def __init__(self, name, parent, text, pos, font, visible, size, spacing, color):
        self.name = name
        self.parent = parent
        self.text = text
        self.pos = pos
        self.font = font
        self.visible = visible
        self.size = size
        self.spacing = spacing
        self.color = color
    
    def engineRender(self, offset):
        fontDat = engine.assets.getFont(self.font)
        size = self.size if self.size > 0 else fontDat.baseSize
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)

        DrawTextEx(fontDat, self.text.encode(), newPos, size, self.spacing, self.color)
