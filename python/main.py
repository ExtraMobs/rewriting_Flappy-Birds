import pygame

from assets_manager import load_assets
from gameengine import resources
from gameengine.core.program import Program
from gameengine.core.window import Display, Window
from scenes.gamescene import GameScene
from scenes.staterscene import StarterScene


class Flappy(Program):
    def __init__(self):
        super().__init__(Window((518, 920)), Display((288, 512)), framerate=60)
        load_assets()
        self.window.set_icon(resources.surface.get("icon"))
        self.window.set_title("Flappy Birds")

        resources.scenes.add(starter=StarterScene, game=GameScene)

        self.set_scene(StarterScene())


if __name__ == "__main__":
    Flappy().start_loop()
