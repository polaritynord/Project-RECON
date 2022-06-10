import engine
from json import load
from os.path import join

class Tree(object):
    def __init__(self):
        self.__children = {}
    
    def __loadSceneNode(self, nodeName, nodeData, parent):
        newNode = engine.Node(parent)
        newNode.name = nodeName
        parent.getChildren()[nodeName] = newNode
        # Add components
        for compName in nodeData["components"]:
            newNode.addComponent(getattr(engine.gameComponents, compName))

        # Add children
        for i, v in nodeData["children"].items():
            self.__loadSceneNode(i, v, newNode)

    def loadScene(self, sceneName):
        with open(join(engine.GAME_NAME, "scenes", sceneName + ".json")) as sc_file:
            sc_data = load(sc_file)

            for i, v in sc_data.items():
                self.__loadSceneNode(i, v, self)
    
    def engineUpdate(self):
        # Update children
        for i, v in self.__children.items():
            v.engineUpdate()

    def getChildren(self):
        return self.__children
    
    def getNode(self, name):
        return self.__children[name]
    
    def addNode(self, nodeObj):
        newNode = nodeObj(self)
        self.__children[newNode.name] = newNode
    
    def removeNode(self, nodeName):
        del self.__children[nodeName]
