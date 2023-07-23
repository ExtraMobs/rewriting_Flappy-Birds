from dataclasses import dataclass

import pygame

from gameengine import resources


@dataclass
class AssetData:
    name: str
    rect: pygame.Rect


def load_assets():
    resources.surface.set(
        "atlas", resources.surface.load_from_file("assets\\gfx\\atlas.png")
    )

    atlas_coords = open("atlas.txt", "r")
    for line in atlas_coords.readlines():
        line = line.strip().split(" ")

        name = line[0]
        rect = pygame.Rect(
            round(float(line[3]) * 1024),
            round(float(line[4]) * 1024),
            round(float(line[5]) * 1024),
            round(float(line[6]) * 1024),
        )

        resources.surface.set(name, resources.surface.slice("atlas", rect)[0])

        # pygame.image.save(resources.surface.get(name), f"assets\\{name}.png")
