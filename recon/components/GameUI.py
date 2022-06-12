from engine import *

class GameUI(UIComponent):
    def eventSetup(self, node):
        """Debug menu canvas
        * contains some useful monitors.
        """
        debug = self.addCanvas("debug", enabled=False, eventUpdate=self.updateDebug)
        debug.addTextLabel("fps", color=(240, 240, 240, 140), size=18)
        debug.addTextLabel("mouse_pos", color=(240, 240, 240, 140), size=18, pos=Vector2(0, 15))
    
    def eventUpdate(self, node):
        self.toggleDebug()

    # Debug menu methods
    def toggleDebug(self):
        if not IsKeyPressed(KEY_F3):
            return
        debug = self.getCanvas("debug")
        debug.enabled = not debug.enabled

    def updateDebug(self, canvas):
        # Framerate
        fpsMonitor = canvas.getElement("fps")
        fpsMonitor.text = f"fps: {GetFPS()}"
        # Mouse Position
        mousePos = canvas.getElement("mouse_pos")
        mousePos.text = f"mouse x: {GetMouseX()} y: {GetMouseY()}"
