import pygame

from gameengine.core.devices import Devices
from gameengine.core.window import Display, Window
from gameengine.nodes.basenode import BaseNode
from gameengine.nodes.basescene import BaseScene

pygame.init()


class TimeManager:
    target_framerate: int
    delta: float
    clock: pygame.Clock

    def __init__(self, target_framerate: int) -> None:
        self.set_framerate(target_framerate)
        self.delta = 1 / target_framerate
        self.clock = pygame.time.Clock()

    def set_framerate(self, new_framerate: int) -> None:
        self.target_framerate = new_framerate

    def update(self) -> None:
        self.delta = self.clock.tick(self.target_framerate) / 1000


class EventsManager:
    uncaught_events: list[pygame.Event]

    def update(self):
        self.uncaught_events = pygame.event.get()


class Program:
    request_quit: bool

    window: Window
    display: Display

    time: TimeManager
    devices: Devices
    event: EventsManager

    scene: BaseScene

    def __init__(
        self, window: Window, display: Display = None, framerate: int = 30
    ) -> None:
        self.request_quit = False
        BaseNode.program = self
        pygame.register_quit(self.quit)
        self.window = window
        self.display = display
        if display is None:
            self.display = Display(window.size)
        self.devices = Devices(self)
        self.time = TimeManager(framerate)
        self.event = EventsManager()

        self.scene = BaseScene()

    def set_scene(self, new_scene: BaseScene) -> None:
        self.scene = new_scene

    def update(self) -> None:
        self.request_quit = len(pygame.event.get(pygame.QUIT)) > 0
        self.devices.update()
        self.event.update()

        self.scene.update()
        if not self.request_quit:
            self.scene.draw()

            self.window.update(self.display)

            self.time.update()

    def quit(self) -> None:
        pass

    def start_loop(self) -> None:
        while not self.request_quit:
            self.update()
        pygame.quit()
