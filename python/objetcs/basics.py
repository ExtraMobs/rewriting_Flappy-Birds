import enum
import math
import random

import numpy

from gameengine import resources
from gameengine.animation import Animation
from gameengine.graphicnode import GraphicNode
from gameengine.scene import BaseScene
from gameengine.shader import FakeShader
from gameengine.timer import Timer


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
            self.rect.centery = self.program.display.rect.centery - 34
        self.rect.centerx = self.program.display.rect.centerx

        self.__temp_int = 0

    def update(self):
        self.__temp_int += 8.25 * self.program.time.delta
        if self.state == Bird.IDLE:
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
        self.timer = Timer(0.1832)
        self.timer.pause()

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
