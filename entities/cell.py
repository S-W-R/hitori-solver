from __future__ import annotations
from typing import NoReturn, TYPE_CHECKING
from entities.cell_type import CellType

if TYPE_CHECKING:
    from geometry.point import Point


class Cell:
    def __init__(self, position: Point, cell_type: CellType, value: int):
        self._position = position
        self._cell_type = cell_type
        self._value = value

    @property
    def position(self) -> Point:
        return self._position

    @property
    def value(self):
        return self._value

    @property
    def cell_type(self) -> CellType:
        return self._cell_type

    @cell_type.setter
    def cell_type(self, value: CellType) -> NoReturn:
        self._cell_type = value

    def __copy__(self) -> 'Cell':
        return Cell(self.position, self.cell_type, self.value)
