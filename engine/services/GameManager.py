import engine
from raylib import *
from os.path import join
from json import load
from importlib import import_module

class GameManager:
    def loadGame(directory):
        # Load stuff
        engine.GAME_NAME = directory
        engine.gameComponents = import_module(f"{directory}.components")
        # Read file
        with open(join(directory, "config.json")) as conf_file:
            conf_data = load(conf_file)

            # Setup window
            SetTargetFPS(60)
            SetConfigFlags(FLAG_MSAA_4X_HINT)
            InitWindow(conf_data["win_size"][0], conf_data["win_size"][1], conf_data["title"].encode())
            SetExitKey(0)

            # Load stuff
            engine.assets.loadFont("default", join("engine", "resources", "RobotoMono-Regular.ttf"))

            # Set icon
            if conf_data["icon_path"] == "":
                return
            iconImg = LoadImage(conf_data["icon_path"].encode())
            SetWindowIcon(iconImg)
            UnloadImage(iconImg)
            # Load default scene
            if not "default_scene" in conf_data:
                return
            engine.tree.loadScene(conf_data["default_scene"])
        
    def runGame():
        while not WindowShouldClose():
            engine.tree.engineUpdate()
            BeginDrawing()
            ClearBackground((16, 49, 120))
            engine.renderer.engineRenderTexture()
            engine.renderer.engineRenderParticle()
            engine.renderer.engineRenderUi()
            EndDrawing()
        
        engine.assets.unloadAll()
        CloseWindow()
