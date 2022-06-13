import engine
from raylib import *
from pyray import Vector2

class Button:
    def __init__(
        self, parent, pos, size, text, font, baseColor, textColor, enabled,
        curve, outline, textSize, spacing
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
        self.visible = True
    
    def engineRender(self, offset):
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)
        rec = (newPos.x, newPos.y, self.size.x, self.size.y)

        # Draw base rectangle
        if self.outline > 0:
            DrawRectangleRoundedLines(rec, self.curve, 5, self.outline, self.baseColor)
        else:
            DrawRectangleRounded(rec, self.curve, 5, self.baseColor)

        # Draw text
        fontDat = engine.assets.getFont(self.font)
        size = self.textSize if self.textSize > 0 else fontDat.baseSize
        # TODO: Add centered text
        DrawTextEx(fontDat, self.text.encode(), newPos, size, self.spacing, self.textColor)
