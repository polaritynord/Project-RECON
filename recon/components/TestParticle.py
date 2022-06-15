from engine import *
from random import randint

class TestParticle(ParticleComponent):
    def eventUpdate(self, node):
        if IsMouseButtonDown(0):
            self.addParticle(
                pos=GetMousePosition(), size=Vector2(20, 20), curve=1,
                color=(randint(200, 245), randint(200, 245), randint(200, 245), 255),
                velocity=Vector2(randint(-1000, 1000), 500), eventUpdate=self.test
            )
    
    def test(self, p):
        delta = GetFrameTime()
        p.velocity.x -= p.velocity.x / 10 * delta
        p.velocity.y += 500 * delta
