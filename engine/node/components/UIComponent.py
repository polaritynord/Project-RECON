from raylib import *
from engine.node.components.Component import Component

class UIComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "UIComponent"
        self.__canvases = {}
    
    def addCanvas(self, name, x=0, y=0):
        pass
