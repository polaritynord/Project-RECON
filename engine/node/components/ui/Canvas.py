import engine
from engine.node.components.ui.element import *
from pyray import Vector2
from raylib import BLACK

class Canvas:
    def __init__(self, parent, pos, enabled, eventUpdate):
        self.parent = parent
        self.pos = pos
        self.enabled = enabled
        self.eventUpdate = eventUpdate
        self.__elements = {}
    
    def getElements(self):
        return self.__elements
    
    def getElement(self, name):
        return self.__elements[name]

    # Element adding methods
    def addTextLabel(
        self, name, text="Sample", pos=Vector2(), font="default", visible=True, size=0,
        spacing=1, color=BLACK
    ):
        element = TextLabel(self, text, pos, font, visible, size, spacing, color)
        self.__elements[name] = element
    
    def addRect(self, name, pos=Vector2(), size=Vector2(10, 10), color=BLACK, curve=0, outline=0):
        element = Rect(self, pos, size, color, curve, outline)
        self.__elements[name] = element
    
    # Update & render elements
    def engineRender(self):
        # Custom update call
        if self.eventUpdate != None:
            self.eventUpdate(self)

        # Render elements
        for i, v in self.__elements.items():
            if not v.visible: continue
            engine.uiRenderer.elements.append(v)
