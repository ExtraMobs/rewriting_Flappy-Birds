import pygame

from gameengine import resources
from objetcs.default import Bird, DefaultScene
from scenes.introduction import Introduction


class GameScene(DefaultScene):
    def __init__(self):
        self.gravity = 480

        self.intro = Introduction()
        super().__init__(Bird.PREPARE, True, self.intro)
        self.fading_shader.timer.unpause()

    def update(self) -> None:
        if self.program.devices.mouse.get_pressed_in_frame(pygame.BUTTON_LEFT):
            in_intro = not self.intro is None
            if in_intro:
                self.intro.kill()
                self.intro = None
                self.bird.state = Bird.PLAYING

        if self.program.devices.keyboard.get_pressed_in_frame(pygame.KEYUP, pygame.K_b):
            self.program.set_scene(resources.scenes.get("starter")())

        super().update()
