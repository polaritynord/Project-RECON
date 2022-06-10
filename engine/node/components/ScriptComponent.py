from engine.node.components.Component import Component

class ScriptComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "ScriptComponent"
