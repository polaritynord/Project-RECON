import engine
from engine.node.components.Component import Component
from engine.node.components.particle.Particle import *

class ParticleComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "ParticleComponent"
        self.__particles = []
        self.count = 0
    
    def removeParticle(self, obj):
        self.__particles.remove(obj)
    
    def clearParticles(self):
        self.__particles = []
    
    def addParticle(
        self, pos=Vector2(480, 270), size=Vector2(10, 10), curve=0, outline=0, color=RED,
        velocity=Vector2(5, 0), sizeVel=Vector2(-1, -1), lifetimeMin=5, lifetimeMax=0,
        eventUpdate=None
    ):
        particle = Particle(self, pos, size, curve, outline, color, velocity, sizeVel, lifetimeMin, lifetimeMax, eventUpdate)
        self.__particles.append(particle)
    
    def engineUpdate(self):
        # Update particles
        for particle in self.__particles:
            particle.engineUpdate()

        # Add particles to renderer list
        engine.renderer.particles.extend(self.__particles)
        self.count = len(self.__particles)
