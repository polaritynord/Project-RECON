# Fun fact: this service doesn't actually render UI,
# it stores elements to be rendered on their own
from raylib import *
from pyray import Vector2

class Renderer:
    def __init__(self):
        self.particles = []
        self.elements = []
        self.textures = []
    
    def engineRendereTexture(self):
        for texture in self.textures:
            pass
    
    def engineRenderParticle(self):
        for particle in self.particles:
            # Calculate offset
            node = particle.parent.parent
            offset = node.getTransform().position

            particle.engineRender(offset)
        self.particles = []
    
    def engineRenderUi(self):
        for element in self.elements:
            # Calculate offset
            canvas = element.parent
            parentPos = canvas.parent.parent.getTransform().position
            offset = Vector2(canvas.pos.x + parentPos.x, canvas.pos.y + parentPos.y)

            element.engineRender(offset)
        self.elements = []
