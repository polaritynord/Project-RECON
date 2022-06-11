
class Canvas:
    def __init__(self, x, y, enabled):
        self.x = x
        self.y = y
        self.__elements = {}
        self.enabled = True
    
    def engineRender(self):
        print("test")
