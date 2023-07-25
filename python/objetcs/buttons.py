import pygame
from gameengine import resources
from gameengine.nodes.basenode import BaseNode
from gameengine.nodes.graphicnode import GraphicNode


class Button(GraphicNode):
    def __init__(self, button_name):
        super().__init__(resources.surface.get(f"button_{button_name}"))
        self.pressed = False

    def on_pressed(self):
        pass

    def update(self):
        mouse_pressed = self.program.devices.mouse.get_pressed(pygame.BUTTON_LEFT)
        if (
            self.hitbox.rect.collidepoint(self.program.devices.mouse.pos)
        ) and not self.pressed:
            self.pressed = self.program.devices.mouse.get_pressed_in_frame(
                pygame.BUTTON_LEFT
            )
        elif self.pressed and not mouse_pressed:
            self.on_pressed()
            self.pressed = False

    def draw(self):
        if self.pressed:
            self.rect.y += 1
            super().draw()
            self.rect.y -= 1
        else:
            super().draw()


class PlayButton(Button):
    def __init__(self):
        super().__init__("play")

        self.rect.x = 20
        self.rect.y = 340

    def on_pressed(self):
        if self.program.scene.fading_shader.timer.paused:
            pygame.mixer.Channel(0).play(resources.sound.get("sfx_swooshing"))
        self.program.scene.fading_shader.timer.unpause()


class ScoreButton(Button):
    def __init__(self):
        super().__init__("score")

        self.rect.right = self.program.display.width - 20
        self.rect.y = 340


class RateButton(Button):
    def __init__(self):
        super().__init__("rate")

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = self.program.display.rect.centery + 14


class StaterButtons(BaseNode):
    def __init__(self):
        super().__init__(PlayButton(), ScoreButton(), RateButton())
