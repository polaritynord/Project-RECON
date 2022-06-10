
class Component(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = type(self).__name__
        self.type = "Component"
