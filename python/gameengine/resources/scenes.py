from typing import Any

from gameengine.nodes.basescene import BaseScene


scenes = {}


def set(name: Any, scene_class: BaseScene) -> None:
    scenes[name] = scene_class


def get(name: Any) -> BaseScene:
    return scenes[name]
