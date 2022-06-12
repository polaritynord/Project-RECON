import engine
from raylib import *
from pyray import Vector2

class Rect:
    def __init__(self, parent, pos, size, color, curve, outline):
        self.parent = parent
        self.pos = pos
        self.size = size
        self.color = color
        self.curve = curve
        self.outline = outline
        self.visible = True
    
    def engineRender(self, offset):
        # Set position (offseted by both canvas & node)
        new_pos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)
        rec = (new_pos.x, new_pos.y, self.size.x, self.size.y)
        if self.outline > 0:
            DrawRectangleRoundedLines(rec, self.curve, 5, self.outline, self.color)
        else:
            DrawRectangleRounded(rec, self.curve, 5, self.color)
