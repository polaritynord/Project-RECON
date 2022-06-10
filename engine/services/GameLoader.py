import engine
from raylib import *
from os.path import join
from json import load

class GameLoader:
    def loadGame(directory):
        with open(join(directory, "config.json")) as conf_file:
            conf_data = load(conf_file)

            SetTargetFPS(60)
            SetConfigFlags(FLAG_WINDOW_RESIZABLE)
            InitWindow(conf_data["win_size"][0], conf_data["win_size"][1], conf_data["title"].encode())
            SetExitKey(0)
    
    def runGame():
        while not WindowShouldClose():
            engine.tree.engineUpdate()
            BeginDrawing()
            ClearBackground((16, 49, 120))
            EndDrawing()
        
        CloseWindow()
