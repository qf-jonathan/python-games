import pygame as pg
from typing import Tuple
from game.interfaces import Event, Screen, Timer


class PygameScreen(Screen):
    def set_size(self, size: int) -> None:
        self.size = size
        self.screen = pg.display.set_mode([size] * 2)
    
    def clear(self):
        self.screen.fill('black')
    
    def draw_scenary(self, tile_size: int):
        for x in range(0, self.size, tile_size):
            pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.size))
        for y in range(0, self.size, tile_size):
            pg.draw.line(self.screen, [50] * 3, (0, y), (self.size, y))
    
    def draw_square(self, color: str, position: Tuple[int, int], size: int):
        pg.draw.rect(self.screen, color, pg.rect.Rect([position[0] + 1, position[1] + 1, size - 2, size - 2]))
    
    def update(self):
        pg.display.flip()


class PygameTimer(Timer):
    def __init__(self) -> None:
        self.clock = pg.time.Clock()

    def delay(self, time: int):
        self.clock.tick(time)
    
    def get_current(self):
        return pg.time.get_ticks()


class PygameEvent(Event):
    def __init__(self):
        self.events = None
    
    def load(self):
        if self.events is not None:
            return
        self.events = set()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.events.add('quit')
            if event.type == pg.KEYDOWN:
                if event.key in [pg.K_w, pg.K_UP]:
                    self.events.add('up')
                if event.key in [pg.K_s, pg.K_DOWN]:
                    self.events.add('down')
                if event.key in [pg.K_a, pg.K_LEFT]:
                    self.events.add('left')
                if event.key in [pg.K_d, pg.K_RIGHT]:
                    self.events.add('right')

    def check(self, event_name: str):
        return event_name in self.events
    
    def clear(self):
        self.events = None

