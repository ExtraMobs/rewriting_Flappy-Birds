import enum
import math
import random

import pygame

from gameengine import resources
from gameengine.animation import Animation
from gameengine.basenode import BaseNode
from gameengine.graphicnode import GraphicNode
from gameengine.scene import BaseScene


class Background(GraphicNode):
    def __init__(self):
        day_or_night = random.choice(["day", "night"])
        super().__init__(resources.surface.get(f"bg_{day_or_night}"))


class Bird(GraphicNode):
    IDLE = enum.auto()

    def __init__(self, state):
        self.state = state
        bird_color = random.choice(range(2))
        super().__init__(
            Animation(
                8,
                resources.surface.get(f"bird{bird_color}_0"),
                resources.surface.get(f"bird{bird_color}_1"),
                resources.surface.get(f"bird{bird_color}_2"),
            )
        )

        if state == Bird.IDLE:
            self.rect.centery = self.program.display.rect.centery - 20
        self.rect.centerx = self.program.display.rect.centerx

        self.__temp_int = 0

    def update(self):
        self.__temp_int += 1
        if self.state == Bird.IDLE:
            # a taxa de tempo é 7.18 (????), esse valor foi coletado através de observação
            self.rect.y += (
                -(math.sin(self.__temp_int / 7.18) * 30) * self.program.time.delta
            )

        if self.animation.frame_index == 2:
            self.animation.reverse = True
        elif self.animation.frame_index == 0:
            self.animation.reverse = False

        super().update()


class Floor(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("land"))
        self.rect.bottom = self.program.display.height

    def update(self):
        self.rect.x += -168 * self.program.time.delta
        self.rect.x %= self.program.display.width - self.rect.w


class CopyrightLabel(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("brand_copyright"))
        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = self.program.display.rect.height - 93


class FlappyTitle(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("title"))

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = 150


class Button(GraphicNode):
    def __init__(self, button_name):
        super().__init__(resources.surface.get(f"button_{button_name}"))
        self.pressed = False

    def on_pressed(self):
        pass

    def update(self):
        super().update()

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


class ScoreButton(Button):
    def __init__(self):
        super().__init__("score")

        self.rect.right = self.program.display.width - 20
        self.rect.y = 340


class RateButton(Button):
    def __init__(self):
        super().__init__("rate")

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = self.program.display.rect.centery + 20


class Buttons(BaseNode):
    def __init__(self):
        super().__init__(PlayButton(), ScoreButton(), RateButton())


class StarterScene(BaseScene):
    def __init__(self):
        super().__init__()

        self.bird = Bird(Bird.IDLE)

        self.add_children(
            Background(), self.bird, Floor(), Buttons(), FlappyTitle(), CopyrightLabel()
        )
