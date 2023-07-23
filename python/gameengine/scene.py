from .basenode import BaseNode


class BaseScene(BaseNode):
    bg = (0, 0, 0)

    def __init__(self, *children):
        super().__init__(*children)
        self.parent = self.program.display

    def draw(self):
        self.surface.fill(self.bg)
        super().draw()
