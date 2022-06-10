from engine.node.components.Component import Component
from pyray import Vector2

class TransformComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.position = Vector2()
        self.scale = 1
        self.rotation = 0
