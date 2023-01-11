from abc import ABC, abstractmethod
from typing import Tuple


class Screen(ABC):
    @abstractmethod
    def set_size(self, size: int) -> None:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def draw_scenary(self, tile_size: int):
        pass

    @abstractmethod
    def draw_square(self, color: str, position: Tuple[int,int], size: int):
        pass

    @abstractmethod
    def update(self):
        pass

class Timer(ABC):
    @abstractmethod
    def delay(self, time: int):
        pass

    @abstractmethod
    def get_current(self):
        pass

class Event(ABC):
    @abstractmethod
    def check(self, event_name: str) -> bool:
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def clear(self):
        pass
