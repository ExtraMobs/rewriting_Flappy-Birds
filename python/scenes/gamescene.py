import pygame

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from objetcs.default import DefaultScene


class TapTip(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("tutorial"))

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.centery = self.program.display.rect.centery + 12


class GetReadyLabel(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("text_ready"))

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.centery = self.program.display.rect.centery - 80


class GameScene(DefaultScene):
    def __init__(self):
        super().__init__(TapTip(), GetReadyLabel())
        self.fading_shader.reversed = True

    def update(self) -> None:
        super().update()

        if self.program.devices.keyboard.get_pressed_in_frame(pygame.KEYUP, pygame.K_b):
            self.program.set_scene(resources.scenes.get("starter")())
