from engine import *
from random import randint

class KeyTest(ScriptComponent):
    def eventSetup(self, node):
        keyboard.addAction("action1", [KEY_SPACE, KEY_F11])

    def eventUpdate(self, node):
        print("please kill me :)")
        if keyboard.isActionPressed("action1"):
            node.remove()
