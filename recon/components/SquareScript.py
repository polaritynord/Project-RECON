from engine import *

class SquareScript(ScriptComponent):
    def eventSetup(self, node):
        assets.loadTexture("square", "recon/resources/square.png")

        node.getComponent("TextureComponent").texture = "square"
