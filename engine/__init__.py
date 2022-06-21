from engine.services import *
from engine.node import *
from enum import Enum

GAME_NAME = ""

gameComponents = None

# Services
renderer = Renderer()
gameManager = GameManager
assets = AssetManager()
tree = Tree()
keyboard = Keyboard()

# Utilities
def getScreenMiddle():
    return Vector2(GetScreenWidth()/2, GetScreenHeight()/2)
