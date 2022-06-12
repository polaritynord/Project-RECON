import engine
from raylib import *
from os.path import join
from json import load
from importlib import import_module

class GameLoader:
    def loadGame(directory):
        with open(join(directory, "config.json")) as conf_file:
            conf_data = load(conf_file)

            # Setup window
            SetTargetFPS(60)
            SetConfigFlags(FLAG_MSAA_4X_HINT)
            InitWindow(conf_data["win_size"][0], conf_data["win_size"][1], conf_data["title"].encode())
            SetExitKey(0)

            # Set icon
            if conf_data["icon_path"] == "":
                return
            iconImg = LoadImage(conf_data["icon_path"].encode())
            SetWindowIcon(iconImg)
            UnloadImage(iconImg)
        
        engine.GAME_NAME = directory
        engine.gameComponents = import_module(f"{directory}.components")
        engine.assets.loadFont("default", join("engine", "resources", "RobotoMono-Regular.ttf"))
    
    def runGame():
        while not WindowShouldClose():
            engine.tree.engineUpdate()
            BeginDrawing()
            ClearBackground((16, 49, 120))
            engine.uiRenderer.engineUpdate()
            EndDrawing()
        
        CloseWindow()
        engine.assets.unloadAll()
