import numpy

from gameengine.utils.shader import FakeShader
from gameengine.utils.timer import Timer


class FadingShader(FakeShader):
    def __init__(self, reversed=False):
        self.timer = Timer(0.4)
        self.timer.pause()
        self.timer.auto_pause = True
        self.reversed = reversed
        super().__init__(self.timer)

    def get_tax(self):
        tax = self.timer.current_time / self.timer.target_time
        return tax if self.reversed else 1 - tax


class FadingBlackShader(FadingShader):
    def draw(self, pixels2d, pixels3d, pixels_alpha):
        if not self.timer.reached and not self.timer.paused:
            tax = self.get_tax()
            numpy.multiply(pixels3d, (tax, tax, tax), pixels3d, casting="unsafe")


class FadingAlpha(FadingShader):
    def draw(self, pixels2d, pixels3d, pixels_alpha):
        tax = self.get_tax()
        numpy.multiply(pixels_alpha, tax, pixels_alpha, casting="unsafe")
