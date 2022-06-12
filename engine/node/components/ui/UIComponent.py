from raylib import *
from pyray import Vector2
from engine.node.components.Component import Component
from engine.node.components.ui.Canvas import Canvas

class UIComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "UIComponent"
        self.__canvases = {}
    
    def addCanvas(self, name, pos=Vector2(), enabled=True, eventUpdate=None):
        canvas = Canvas(self, pos, enabled, eventUpdate)
        self.__canvases[name] = canvas
        return canvas
    
    def getCanvas(self, name):
        return self.__canvases[name]
    
    def engineUpdate(self):
        for i, v in self.__canvases.items():
            if not v.enabled:
                continue
            v.engineRender()
