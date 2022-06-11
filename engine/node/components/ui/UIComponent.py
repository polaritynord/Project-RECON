from raylib import *
from engine.node.components.Component import Component
from engine.node.components.ui.Canvas import Canvas

class UIComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "UIComponent"
        self.__canvases = {}
    
    def addCanvas(self, name, x=0, y=0, enabled=True):
        self.__canvases[name] = Canvas(x, y, enabled)
    
    def engineUpdate(self):
        for i, v in self.__canvases.items():
            if not v.enabled:
                continue
            v.engineRender()
