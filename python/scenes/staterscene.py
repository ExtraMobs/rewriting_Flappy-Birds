from gameengine import resources
from gameengine.graphicnode import GraphicNode
from objetcs.basics import DefaultScene
from objetcs.buttons import StaterButtons


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
        super().__init__(StaterButtons(), FlappyTitle(), CopyrightLabel())
