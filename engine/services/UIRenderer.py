# Fun fact: this service doesn't actually render UI,
# it stores elements to be rendered on their own
from raylib import *
from pyray import Vector2

class UIRenderer:
    def __init__(self):
        self.textLabels = []
    
    def engineUpdate(self):
        for element in self.textLabels:
            # Calculate offset
            canvas = element.parent
            parent_pos = canvas.parent.parent.getTransform().position
            offset = Vector2(canvas.pos.x + parent_pos.x, canvas.pos.y + parent_pos.y)

            element.engineRender(offset)
        self.textLabels = []
