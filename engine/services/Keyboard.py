from raylib import *

class Keyboard:
    def __init__(self):
        self.__actions = {}
    
    def isActionPressed(self, name):
        for key in self.__actions[name]:
            if IsKeyPressed(key):
                return True
        return False
    
    def isActionDown(self, name):
        for key in self.__actions[name]:
            if IsKeyDown(key):
                return True
        return False
    
    def isActionReleased(self, name):
        for key in self.__actions[name]:
            if IsKeyReleased(key):
                return True
        return Falses
    
    def isActionUp(self, name):
        for key in self.__actions[name]:
            if IsKeyDown(key):
                return False
        return True
    
    def addAction(self, name, keys):
        # If only one key is given:
        self.__actions[name] = [keys] if type(keys) == int else keys
    
    def removeAction(self, name):
        del self.__actions[name]
