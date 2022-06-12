This directory contains some of the services the game requires to run.

Each service & their uses:
* AssetManager: Contains fonts, textures, sounds; and unloads them from memory.
* GameManager: Sets up the window & runs.
* Tree: The root node for all nodes. Also manages scene loading.
* Keyboard: Checks for key input (mostly a wrapper for raylib, with more stuff)