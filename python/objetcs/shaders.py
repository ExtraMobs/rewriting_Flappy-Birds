import numpy
import pygame

from gameengine.misc.shader import FakeShader
from gameengine.misc.timer import Timer


class FadingShader(FakeShader):
    def __init__(self, time, reversed=False):
        self.timer = Timer(time)
        self.timer.pause()
        self.timer.auto_pause = True
        self.reversed = reversed
        super().__init__(self.timer)

    def get_tax(self):
        tax = self.timer.current_time / self.timer.target_time
        return tax if self.reversed else 1 - tax


class FadingBlackShader(FadingShader):
    def __init__(self, reversed):
        super().__init__(0.4, reversed)

    def draw(self, surf):
        surf_array = pygame.surfarray.pixels3d(surf)
        if not self.timer.reached and not self.timer.paused:
            tax = self.get_tax()
            numpy.multiply(surf_array, (tax, tax, tax), surf_array, casting="unsafe")


class FadingAlpha(FadingShader):
    def __init__(self):
        super().__init__(0.4)

    def draw(self, surf):
        pixels_alpha = pygame.surfarray.pixels_alpha(surf)
        tax = self.get_tax()
        numpy.multiply(pixels_alpha, tax, pixels_alpha, casting="unsafe")
