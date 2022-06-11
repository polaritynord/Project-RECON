from raylib import *
from pyray import Vector2

class TextLabel:
    def __init__(self, parent, text, pos, font, visible):
        self.parent = parent
        self.text = text
        self.pos = pos
        self.font = font
        self.visible = visible
    
    def engineRender(self):
        pass
