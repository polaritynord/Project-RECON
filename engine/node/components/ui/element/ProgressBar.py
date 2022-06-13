import engine
from raylib import *
from pyray import Vector2

class ProgressBar:
    def __init__(self, name, parent, pos, size, color, value, type, begin):
        self.name = name
        self.parent = parent
        self.pos = pos
        self.size = size
        self.color = color
        self.value = value
        self.type = type
        self.begin = begin
        self.visible = True

    def engineRender(self, offset):
        if not self.visible:
            return
        
        # Horizontal bar
        if self.type == "h":
            pass
        else:
            # Vertical bar
            pass
            
