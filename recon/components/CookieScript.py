from engine import *

class CookieScript(ScriptComponent):
    def eventSetup(self, node):
        # Load resources
        assets.loadTexture("cookie", "recon/resources/cookie.png")
        # Set texture
        texture = node.getComponent("TextureComponent")
        texture.texture = "cookie"
        # Set transform properties
        transform = node.getTransform()
        transform.scale = Vector2(1.6, 1.6)
        transform.position = getScreenMiddle()
    
    def eventUpdate(self, node):
        pass
