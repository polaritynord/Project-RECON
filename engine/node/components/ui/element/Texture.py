import engine
from raylib import *
from pyray import Vector2

class Texture:
    def __init__(self, name, parent, pos, texture, scale, rotation):
        self.name = name
        self.parent = parent
        self.pos = pos
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.visible = True
    
    def engineRender(self, offset):
        if not self.visible:
            return
        # Set position (offseted by both canvas & node)
        textureDat = engine.assets.getTexture(self.texture)
        newPos = Vector2(self.pos.x + offset.x, self.pos.y + offset.y)

        fw = textureDat.width * self.scale.x
        fh = textureDat.height * self.scale.y
        source = (0, 0, fw, fh)
        dest = (newPos.x, newPos.y, fw, fh)
        origin = (fw/2, fh/2)

        DrawTexturePro(textureDat, source, dest, origin, self.rotation, WHITE)

        #DrawTextureEx(textureDat, newPos, self.rotation, self.scale, WHITE)
