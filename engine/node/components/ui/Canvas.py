from engine.node.components.ui.element import *
from pyray import Vector2

class Canvas:
    def __init__(self, pos, enabled, eventUpdate):
        self.pos = pos
        self.__elements = {}
        self.enabled = True
        self.eventUpdate = eventUpdate
    
    def addTextLabel(self, text="Sample", pos=Vector2(), font="default", visible=True):
        pass
    
    def engineRender(self):
        if self.eventUpdate != None:
            self.eventUpdate(self)
