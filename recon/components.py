from engine import *

class TestScript(ScriptComponent):
    def eventUpdate(self):
        node = self.parent
        print(node.getTransform().rotation)
        node.getTransform().rotation += 1
