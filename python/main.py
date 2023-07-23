import pygame
from assets_manager import load_assets
from gameengine import resources
from gameengine.engine import Program
from gameengine.window import Display, Window
from scenes.staterscene import StarterScene


class Flappy(Program):
    def __init__(self):
        super().__init__(Window((432, 768)), Display((288, 512)), framerate=60)
        self.window.set_icon(resources.surface.load_from_file("assets\\gfx\\ic_launcher.png"))
        self.window.set_title("Flappy Birds")
        load_assets()

        self.set_scene(StarterScene())


if __name__ == "__main__":
    Flappy().start_loop()
