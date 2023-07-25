import pygame

from .basenode import BaseNode


class ShadingManager(BaseNode):
    def add_shader(self, *new_shaders) -> None:
        self.add_children(*new_shaders)

    def draw(self, surf: pygame.Surface) -> None:
        for shader in self.children:
            shader.draw(
                pygame.surfarray.pixels2d(surf), pygame.surfarray.pixels3d(surf)
            )


class ShadingNode(BaseNode):
    def __init__(self, *children) -> None:
        super().__init__(*children)
        self.shader_manager = ShadingManager()

    def update(self) -> None:
        super().update()
        self.shader_manager.update()

    def draw(self) -> None:
        super().draw()
        self.shader_manager.draw(self.surface)
