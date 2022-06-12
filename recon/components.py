from engine import *

class TestUI(UIComponent):
    def eventSetup(self, node):
        canvas = self.addCanvas("canvas", eventUpdate=self.test)
        canvas.addTextLabel("text", size=18, color=(225, 225, 225, 255))
        canvas.addRect(
            "rect", size=Vector2(55, 55), pos=Vector2(GetScreenWidth()/2, GetScreenHeight()/2)
        )
    
    def test(self, canvas):
        textLabel = canvas.getElement("text")
        textLabel.text = f"FPS: {engine.GetFPS()}"
