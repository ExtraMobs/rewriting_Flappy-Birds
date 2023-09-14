from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode
from gameengine.nodes.node import Node
from objetcs.shaders import FadingAlpha


class IntroductionNode(GraphicNode):
    def __init__(self, name):
        super().__init__(resources.surface.get(name))
        self.fading_shader = FadingAlpha()
        self.add_shader(self.fading_shader)


class TapTip(IntroductionNode):
    def __init__(self):
        super().__init__("tutorial")

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.centery = self.program.display.rect.centery + 12


class GetReadyLabel(IntroductionNode):
    def __init__(self):
        super().__init__("text_ready")

        self.rect.centerx = self.program.display.rect.centerx
        self.rect.centery = self.program.display.rect.centery - 80


class Introduction(Node):
    def __init__(self):
        super().__init__(TapTip(), GetReadyLabel())
