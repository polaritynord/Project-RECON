from raylib import *
from pyray import Vector2

class Particle:
    def __init__(
        self, parent, pos, size, curve, outline, color, velocity, sizeVel, lifetimeMin,
        lifetimeMax, eventUpdate
    ):
        self.parent = parent
        self.pos = pos
        self.size = size
        self.curve = curve
        self.outline = outline
        self.color = color
        self.velocity = velocity
        self.sizeVel = sizeVel
        self.lifetimeMin = lifetimeMin
        self.lifetimeMax = lifetimeMax
        self.eventUpdate = eventUpdate
        self.__timer = GetTime()
    
    def engineRender(self):
        pass
