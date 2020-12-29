from typing import Iterable

from conflict_finder.conflict import Conflict
from conflict_finder.conflict_type import ConflictType
from geometry.point import Point


class LineConflict(Conflict):
    CONFLICT_TYPE = ConflictType.MORE_THAN_ONE_IN_LINE

    def __init__(self, points: Iterable[Point]):
        self._points = list(points)

    @property
    def conflict_type(self) -> ConflictType:
        return self.CONFLICT_TYPE

    @property
    def points(self) -> Iterable[Point]:
        return self._points
