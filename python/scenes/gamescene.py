import pygame

from gameengine import resources
from objetcs.default import Bird, DefaultScene
from scenes.introduction import Introduction


class GameScene(DefaultScene):
    def __init__(self):
        super().__init__(Bird(Bird.PREPARE), True, Introduction())
        self.fading_shader.timer.unpause()

    def update(self) -> None:
        super().update()

        if self.program.devices.mouse.get_pressed_in_frame(pygame.BUTTON_LEFT):
            ...

        if self.program.devices.keyboard.get_pressed_in_frame(pygame.KEYUP, pygame.K_b):
            self.program.set_scene(resources.scenes.get("starter")())
