from engine.services import *
from engine.node import *
from enum import Enum

GAME_NAME = ""

gameComponents = None

# Services
uiRenderer = UIRenderer()
gameManager = GameManager
assets = AssetManager()
tree = Tree()
keyboard = Keyboard()
