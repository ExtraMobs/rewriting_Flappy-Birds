import enum
import math
import random

from gameengine import resources
from gameengine.nodes.basescene import BaseScene
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.utils.animation import Animation
from objetcs.shaders import FadingBlackShader


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

        self.__playing = False

        self.__temp_int = 0

    def update(self):
        if not self.__playing:
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


class DefaultScene(BaseScene):
    def __init__(self, *children):
        self.bird = Bird(Bird.IDLE)
        self.fading_shader = FadingBlackShader()

        super().__init__(Background(), self.bird, Floor(), *children)

        self.add_shader(self.fading_shader)
