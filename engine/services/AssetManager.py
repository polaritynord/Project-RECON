from raylib import *

class AssetManager:
    def __init__(self):
        self.__fonts = {}
    
    def loadFont(self, name, path):
        self.__fonts[name] = LoadFont(path.encode())
    
    def unloadFont(self, name):
        UnloadFont(self.__fonts[name])
        del self.__fonts[name]
    
    def getFont(self, name):
        return self.__fonts[name]
    
    def unloadAll(self):
        # Unload fonts
        for i in self.__fonts.copy():
            self.unloadFont(i)
