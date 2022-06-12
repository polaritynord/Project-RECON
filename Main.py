from engine import *

def main():
    gameManager.loadGame("recon")
    tree.loadScene("scene_game")
    gameManager.runGame()

if __name__ == "__main__":
    main()
