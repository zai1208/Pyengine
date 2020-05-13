import pygame

class Pyengine(WIDTH, HEIGHT, GAME_TYPE="plain", WORLD_TYPE="2D", *args, **kwargs):
     screen = pygame.display.set_mode((WIDTH, HEIGHT))
     if WORLD_TYPE == "2D":
         import UI2D
     elif WORLD_TYPE == "3D":
         import UI3D
     GAME_TYPES = ["plain", "retro", "modern", "futuristic"]
     if GAME_TYPE not in GAME_TYPES:
         print("Error: GAME_TYPE supplied is not supported")
