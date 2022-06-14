from engine import *

class TestParticle(ParticleComponent):
    def eventUpdate(self, node):
        print(node)
