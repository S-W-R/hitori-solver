from abc import ABC, abstractmethod
from collections import Iterable

from conflict_finder.conflict_type import ConflictType
from geometry.point import Point


class Conflict(ABC):
    @property
    @abstractmethod
    def conflict_type(self) -> ConflictType:
        pass

    @property
    @abstractmethod
    def points(self) -> Iterable[Point]:
        pass
