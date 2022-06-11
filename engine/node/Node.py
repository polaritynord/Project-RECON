from engine.node.components import TransformComponent
from pyray import Vector2

class Node(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = type(self).__name__
        self.__children = {}
        self.__components = {}
        self.addComponent(TransformComponent)
    
    # TransformComponent related stuff
    def getTransform(self):
        return self.getComponent("TransformComponent")
    
    # Engine update
    def engineUpdate(self):
        # Update children
        for i, v in self.getChildren().items():
            v.engineUpdate()
        
        # Update components
        for i, v in self.getComponents().items():
            # Engine related calls
            if hasattr(v, "engineUpdate"):
                v.engineUpdate()
            # Calls based on component type
            if v.type == "ScriptComponent" and hasattr(v, "eventUpdate"):
                v.eventUpdate()
    
    # Node-related methods
    def getChildren(self):
        return self.__children
    
    def getNode(self, name):
        return self.__children[name]
    
    def addNode(self, nodeObj):
        newNode = nodeObj(self)
        self.__children[newNode.name] = newNode
    
    def removeNode(self, nodeName):
        del self.__children[nodeName]

    # Component-related methods
    def getComponent(self, compName):
        return self.__components[compName]
    
    def getComponents(self):
        return self.__components
    
    def hasComponentName(self, compName):
        return compName in self.__components.keys()
    
    def hasComponent(self, compType):
        for i, v in self.getComponents():
            if v.type == compType:
                return True
        return False
    
    def addComponent(self, compObj):
        newComp = compObj(self)
        self.__components[newComp.name] = newComp
    
    def removeComponent(self, compName):
        del self.__components[compName]
