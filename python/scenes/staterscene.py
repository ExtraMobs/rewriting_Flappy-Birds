import numpy

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from objetcs.buttons import StaterButtons
from objetcs.default import Bird, DefaultScene


class CopyrightLabel(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("brand_copyright"))
        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = self.program.display.rect.height - 94


class FlappyTitle(GraphicNode):
    def __init__(self):
        super().__init__(resources.surface.get("title"))

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.y = 150


class StarterScene(DefaultScene):
    def __init__(self):
        super().__init__(
            Bird(Bird.IDLE), False, StaterButtons(), FlappyTitle(), CopyrightLabel()
        )

        self.a = numpy.zeros((10000, 10000, 3))
        self.a.fill(255)

    def update(self):
        super().update()
        if self.fading_shader.timer.reached:
            self.program.set_scene(resources.scenes.get("game")())
            del self
