from engine import *

class TestUI(UIComponent):
    def eventSetup(self, node):
        canvas = self.addCanvas("canvas", eventUpdate=self.test)
        canvas.addTextLabel("text", size=24)
    
    def test(self, canvas):
        canvas.getElement("text").text = f"FPS: {engine.GetFPS()}"
