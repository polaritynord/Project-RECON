from engine.node.components.Component import Component
from engine.node.components.particle.Particle import *

class ParticleComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "ParticleComponent"
        self.__particles = []
    
    def clearParticles(self):
        self.__particles = []
    
    def engineUpdate(self):
        print("test")
