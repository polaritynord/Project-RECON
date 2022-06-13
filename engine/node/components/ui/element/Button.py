import engine
from raylib import *
from pyray import Vector2

class Button:
    def __init__(
        self, parent, pos, size, text, font, baseColor, textColor, enabled,
        curve, outline, textSize, spacing, focusColor, clickColor
    ):
        self.parent = parent
        self.pos = pos
        self.size = size
        self.textSize = textSize
        self.text = text
        self.font = font
        self.baseColor = baseColor
        self.textColor = textColor
        self.enabled = enabled
        self.curve = curve
        self.outline = outline
        self.spacing = spacing
        self.focusColor = focusColor
        self.clickColor = clickColor
        self.__realBaseColor = baseColor
        self.__realTextColor = textColor
        self.visible = True
    
    def engineUpdate(self):
        if not self.enabled:
            return
        mouse = GetMousePosition()
        touch = mouse.x > self.pos.x and mouse.x - self.size.x < self.pos.x and mouse.y > self.pos.y and mouse.y - self.size.y < self.pos.y

        if touch:
            bc = self.baseColor
            fc = self.focusColor
            self.__realBaseColor = (abs(bc[0]-fc), abs(bc[1]-fc), abs(bc[2]-fc), bc[3])

            tc = self.textColor
            self.__realTextColor = (abs(tc[0]-fc), abs(tc[1]-fc), abs(tc[2]-fc), tc[3])
        else:
            self.__realBaseColor = self.baseColor
    
    def engineRender(self, offset):
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)
        rec = (newPos.x, newPos.y, self.size.x, self.size.y)

        # Draw base rectangle
        if self.outline > 0:
            DrawRectangleRoundedLines(rec, self.curve, 5, self.outline, self.__realBaseColor)
        else:
            DrawRectangleRounded(rec, self.curve, 5, self.__realBaseColor)

        # Draw text
        fontDat = engine.assets.getFont(self.font)
        size = self.textSize if self.textSize > 0 else fontDat.baseSize
        # TODO: Add centered text
        DrawTextEx(fontDat, self.text.encode(), newPos, size, self.spacing, self.__realTextColor)
