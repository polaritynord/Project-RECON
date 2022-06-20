from raylib import *
from pyray import Vector2

class Slider:
    def __init__(
        self, name, parent, pos, value, baseWidth, baseHeight,
        baseColor, sliderColor, sliderWidth, sliderHeight
    ):
        self.name = name
        self.parent = parent
        self.pos = pos
        self.value = value
        self.baseWidth = baseWidth
        self.baseHeight = baseHeight
        self.baseColor = baseColor
        self.sliderColor = sliderColor
        self.sliderWidth = sliderWidth
        self.sliderHeight = sliderHeight
        self.visible = True
    
    def engineUpdate(self):
        pass

    def engineRender(self, offset):
        print("nice")
