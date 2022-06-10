
class Node(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = type(self).__name__
        self.__children = {}
        self.__components = {}
    
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
