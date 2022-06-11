from engine import *

class TestUI(UIComponent):
    def eventSetup(self, node):
        self.addCanvas("canvas", eventUpdate=self.test)
    
    def test(self, canvas):
        print("aa")
