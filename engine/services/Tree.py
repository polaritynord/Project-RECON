
class Tree(object):
    def __init__(self):
        self.__children = {}
    
    def engineUpdate(self):
        # Update children
        for i, v in self.__children.items():
            v.engineUpdate()

    def getChildren(self):
        return self.__children.values()
    
    def getNode(self, name):
        return self.__children[name]
    
    def addNode(self, nodeObj):
        newNode = nodeObj(self)
        self.__children[newNode.name] = newNode
    
    def removeNode(self, nodeName):
        del self.__children[nodeName]
