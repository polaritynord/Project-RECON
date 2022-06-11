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

    def addTextLabel(
        self, name, text="Sample", pos=Vector2(), font="default", visible=True, size=0,
        spacing=1, color=BLACK
    ):
        element = TextLabel(self, text, pos, font, visible, size, spacing, color)
        self.__elements[name] = element
    
    def engineRender(self):
        # Custom update call
        if self.eventUpdate != None:
            self.eventUpdate(self)

        # Render elements
        for i, v in self.__elements.items():
            if not v.visible: continue
            engine.uiRenderer.textLabels.append(v)
