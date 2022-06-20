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
        self.__touch = False
    
    def engineUpdate(self):
        # Slider rec
        sliderX = self.pos.x + self.value * self.baseWidth
        sliderY = self.pos.y - abs(self.baseHeight - self.sliderHeight)/2
        sliderRec = (sliderX, sliderY, self.sliderWidth, self.sliderHeight)

        # Check for slider collision & set value

        if IsMouseButtonDown(0):
            if self.__touch:
                newX = GetMouseX() - self.pos.x - self.sliderWidth/2
                # Limit new x to the base
                if newX < 0:
                    newX = 0
                elif newX > self.baseWidth:
                    newX = self.baseWidth
                
                self.value = newX / self.baseWidth
        else:
            self.__touch = CheckCollisionPointRec(GetMousePosition(), sliderRec)

    def engineRender(self, offset):
        if not self.visible:
            return
        
        # Set position (offseted by both canvas & node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)

        # Base rec
        baseRec = (self.pos.x, self.pos.y, self.baseWidth, self.baseHeight)
        # Slider rec
        sliderX = self.pos.x + self.value * self.baseWidth
        sliderY = self.pos.y - abs(self.baseHeight - self.sliderHeight)/2
        sliderRec = (sliderX, sliderY, self.sliderWidth, self.sliderHeight)

        # Draw base
        DrawRectangleRec(baseRec, self.baseColor)
        # Draw slider
        DrawRectangleRec(sliderRec, self.sliderColor)
