from engine import *
from random import randint

class KeyTest(ScriptComponent):
    def eventSetup(self, node):
        keyboard.addAction("action1", [KEY_SPACE, KEY_F11])

    def eventUpdate(self, node):
        if keyboard.isActionUp("action1"):
            print(randint(0, 5))
