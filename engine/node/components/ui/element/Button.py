import engine
from raylib import *
from pyray import Vector2

class Button:
    def __init__(
        self, name, parent, pos, size, text, font, baseColor, textColor, enabled,
        curve, outline, textSize, spacing, focusColor, clickColor, triggerPress
    ):
        self.name = name
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
        self.triggerPress = triggerPress
        self.__realBaseColor = baseColor
        self.__realTextColor = textColor
        self.visible = True
    
    def engineUpdate(self):
        if not self.enabled:
            return
        mouse = GetMousePosition()
        touch = mouse.x > self.pos.x and mouse.x - self.size.x < self.pos.x and mouse.y > self.pos.y and mouse.y - self.size.y < self.pos.y
        click = touch and IsMouseButtonDown(0)

        # Visual effects
        bc = self.baseColor
        fc = self.focusColor
        cc = self.clickColor
        tc = self.textColor

        self.__realBaseColor = self.baseColor
        self.__realTextColor = self.textColor

        if touch:
            self.__realBaseColor = (abs(bc[0]-fc), abs(bc[1]-fc), abs(bc[2]-fc), bc[3])
            self.__realTextColor = (abs(tc[0]-fc), abs(tc[1]-fc), abs(tc[2]-fc), tc[3])
        
        if click:
            self.__realBaseColor = (abs(bc[0]-cc), abs(bc[1]-cc), abs(bc[2]-cc), bc[3])
            self.__realTextColor = (abs(tc[0]-cc), abs(tc[1]-cc), abs(tc[2]-cc), tc[3])

        # Trigger button press
        node = self.parent.parent
        if (touch and IsMouseButtonReleased(0)) and self.triggerPress != None:
            self.triggerPress()
    
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
