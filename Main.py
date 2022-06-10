from engine import *

def main():
    gameLoader.loadGame("recon")
    tree.loadScene("scene_game")
    gameLoader.runGame()

if __name__ == "__main__":
    main()
