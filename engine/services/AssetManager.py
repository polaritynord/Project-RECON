from raylib import *

class AssetManager:
    def __init__(self):
        self.__textures = {}
        self.__fonts = {}
    
    def loadFont(self, name, path):
        self.__fonts[name] = LoadFont(path.encode())
    
    def unloadFont(self, name):
        UnloadFont(self.__fonts[name])
        del self.__fonts[name]
    
    def getFont(self, name):
        return self.__fonts[name]
    
    def loadTexture(self, name, path):
        self.__textures[name] = LoadTexture(path.encode())
    
    def unloadTexture(self, name):
        UnloadTexture(self.___textures[name])
        del self.__textures[name]
    
    def getTexture(self, name):
        return self.__textures[name]
    
    def unloadAll(self):
        # Unload fonts
        for i in self.__fonts.copy():
            self.unloadFont(i)
        # Unload textures
        for i in self.__textures.copy():
            self.unloadTexture(i)
