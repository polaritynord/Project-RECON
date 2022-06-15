from raylib import *
from pyray import Vector2
from random import uniform

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
        self.eventUpdate = eventUpdate
        self.__timer = GetTime()
        # Set lifetime
        if lifetimeMax == 0:
            # Fixed lifetime
            self.lifetime = lifetimeMin
        else:
            # Random lifetime
            self.lifetime = uniform(lifetimeMin, lifetimeMax)
        
    def remove(self):
        self.parent.removeParticle(self)
        
    def engineUpdate(self):
        delta = GetFrameTime()
        # Delete past lifetime
        if GetTime() - self.__timer > self.lifetime:
            self.remove()
            return
        # Custom update
        if self.eventUpdate != None:
            self.eventUpdate(self)
        # Position
        self.pos.x += self.velocity.x * delta
        self.pos.y += self.velocity.y * delta
        # Size
        self.size.x += self.sizeVel.x * delta
        self.size.y += self.sizeVel.y * delta
    
    def engineRender(self, offset):
        # Return if too small to be seen
        if self.size.x + self.size.y < 0.01:
            return
        # Set position (offseted by node)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)

        fw = self.size.x
        fh = self.size.y
        source = (0, 0, fw, fh)
        dest = (newPos.x, newPos.y, fw, fh)
        origin = (fw/2, fh/2)
        rec = (newPos.x-self.size.x/2, newPos.y-self.size.y/2, self.size.x, self.size.y)

        if self.outline > 0:
            DrawRectangleRoundedLines(rec, self.curve, 5, self.outline, tuple(self.color))
        else:
            DrawRectangleRounded(rec, self.curve, 5, tuple(self.color))
