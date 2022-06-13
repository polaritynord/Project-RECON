from engine import *
from raylib import *

class Button:
    def __init__(
        self, parent, pos, size, text, font, baseColor, textColor, enabled,
        curve, outline
    ):
        self.parent = parent
        self.pos = pos
        self.size = size
        self.text = text
        self.font = font
        self.baseColor = baseColor
        self.textColor = textColor
        self.enabled = enabled
        self.curve = curve
        self.outline = outline
        self.visible = True
    
    def engineRender(self, offset):
        print("done")
