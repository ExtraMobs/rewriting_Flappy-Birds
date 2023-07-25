from objetcs.default import DefaultScene


class GameScene(DefaultScene):
    def __init__(self, *children):
        super().__init__(*children)
        self.fading_shader.reversed = True
