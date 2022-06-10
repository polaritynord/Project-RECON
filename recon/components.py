from engine import *

class TestScript(ScriptComponent):
    def eventUpdate(self):
        node = self.parent
        node.setRotation(node.getRotation() + 1)
        print(node.getRotation())
