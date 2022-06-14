from engine.node.components.Component import Component

class ParticleComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "ParticleComponent"
