from raylib import *
from pyray import Vector2

class Checkbox:
    def __init__(self, name, parent, pos, size, value, outline, color, curve):
        self.name = name
        self.parent = parent
        self.pos = pos
        self.size = size
        self.outline = outline
        self.color = color
        self.curve = curve
        self.visible = True
        # This enabled decides if the checkbox is full!!
        self.value = value
    
    def engineUpdate(self):
        mouse = GetMousePosition()
        touch = mouse.x > self.pos.x and mouse.x - self.size.x < self.pos.x and mouse.y > self.pos.y and mouse.y - self.size.y < self.pos.y
        
        if touch and IsMouseButtonPressed(0):
            self.value = not self.value
    
    def engineRender(self, offset):
        if not self.visible:
            return
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)
        rec = (newPos.x, newPos.y, self.size.x, self.size.y)

        DrawRectangleRoundedLines(rec, self.curve, 5, self.outline, self.color)
        if self.value:
            DrawRectangleRounded(rec, self.curve, 5, self.color)
