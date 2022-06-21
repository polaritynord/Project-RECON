from engine.node.components.Component import Component
from pyray import Vector2

class TransformComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.position = Vector2()
        self.scale = Vector2(1, 1)
        self.rotation = 0
        # Transform components can't be disabled / removed.
        delattr(self, "enabled")
