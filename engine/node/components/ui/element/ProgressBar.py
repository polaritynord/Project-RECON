import engine
from raylib import *
from pyray import Vector2

class ProgressBar:
    def __init__(self, name, parent, pos, size, backColor, foreColor, value, type, begin):
        self.name = name
        self.parent = parent
        self.pos = pos
        self.size = size
        self.backColor = backColor
        self.foreColor = foreColor
        self.value = value
        self.type = type
        self.begin = begin
        self.visible = True

    def engineRender(self, offset):
        if not self.visible:
            return
        
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)
        rec = (newPos.x, newPos.y, self.size.x, self.size.y)

        # Horizontal bar
        if self.type == "h":
            # Calculate bar position with begin attr
            """
            if self.begin == "left":
                barPos = newPos
            elif self.begin == "right":
                barPos = Vector2(newPos.x + self.size.x, newPos.y)"""

            # Background
            DrawRectangleRec(rec, self.backColor)

            # Bar width calculation
            val = self.value
            if val > 1:
                val = 1
            elif val < 0:
                val = 0
            barW = self.size.x * val
            
            # Foreground
            if self.begin == "left":
                DrawRectangleV(newPos, (barW, self.size.y), self.foreColor)
            elif self.begin == "right":
                DrawRectangleV((newPos.x + self.size.x - barW, newPos.y), (barW, self.size.y), self.foreColor)
            elif self.begin == "middle":
                DrawRectangleV((newPos.x + (self.size.x - barW)/2, newPos.y), (barW, self.size.y), self.foreColor)
            
        else:
            # TODO: Vertical bar
            pass
            
