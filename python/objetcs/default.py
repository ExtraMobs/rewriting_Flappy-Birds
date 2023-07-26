import enum
import math
import random

import numpy

from gameengine import resources
from gameengine.nodes.basescene import BaseScene
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.utils.animation import Animation
from gameengine.utils.shader import FakeShader
from gameengine.utils.timer import Timer


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

        if self.program.scene.__class__.__name__ == "BaseScene":
            self.rect.centery = self.program.display.rect.centery - 35
            self.rect.centerx = self.program.display.rect.centerx
        elif self.program.scene.__class__.__name__ == "StarterScene":
            self.rect.centery = self.program.display.rect.centery - 5
            self.rect.centerx = self.program.display.rect.centerx - 55

        self.__temp_int = 0

    def update(self):
        if self.state == Bird.IDLE:
            self.__temp_int += 8.25 * self.program.time.delta
            self.rect.y += math.sin(self.__temp_int) * (30 * self.program.time.delta)

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
        self.rect.x += -120 * self.program.time.delta
        self.rect.x %= self.program.display.width - self.rect.w


class FadingShader(FakeShader):
    def __init__(self):
        self.timer = Timer(0.4)
        self.timer.auto_pause = True
        self.reversed = False

        super().__init__(self.timer)

    def draw(self, pixels2d, pixels3d):
        if not self.timer.reached and not self.timer.paused:
            tax = self.timer.current_time / self.timer.target_time
            if not self.reversed:
                tax = 1 - tax
            numpy.multiply(pixels3d, (tax, tax, tax), pixels3d, casting="unsafe")


class DefaultScene(BaseScene):
    def __init__(self, *children):
        self.bird = Bird(Bird.IDLE)
        self.fading_shader = FadingShader()

        super().__init__(Background(), self.bird, Floor(), *children)

        self.shader_manager.add_shader(self.fading_shader)
