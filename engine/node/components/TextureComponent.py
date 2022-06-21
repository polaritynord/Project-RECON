import engine
from raylib import *
from engine.node.components.Component import Component

class TextureComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
        self.type = "TextureComponent"
        self.texture = None
    
    def engineUpdate(self):
        if not self.enabled or self.texture == None:
            return
        # Add self to renderer queue
        engine.renderer.textures.append(self)
    
    def engineRender(self, transform):
        # Set position (offseted by both canvas & node)
        textureDat = engine.assets.getTexture(self.texture)

        fw = textureDat.width * transform.scale.x
        fh = textureDat.height * transform.scale.y
        source = (0, 0, textureDat.width, textureDat.height)
        dest = (transform.position.x, transform.position.y, fw, fh)
        origin = (fw/2, fh/2)

        DrawTexturePro(textureDat, source, dest, origin, transform.rotation, WHITE)
