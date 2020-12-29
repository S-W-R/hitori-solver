from typing import List, NoReturn, TypeVar, Generic, Iterable
from geometry.point import Point

T = TypeVar('T')


class Matrix(Generic[T]):
    value: T

    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            raise ValueError()
        self._width = width
        self._height = height
        self._matrix = self.__init_matrix(self._width, self._height)

    @staticmethod
    def __init_matrix(width: int, height: int) -> List[List[T]]:
        matrix = list()
        for i in range(width):
            column = list()
            matrix.append(column)
            for j in range(height):
                column.append(None)
        return matrix

    @staticmethod
    def from_point(point: Point) -> 'Matrix':
        return Matrix(point.x, point.y)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def iterate_over_row(self, row_number: int) -> Iterable[T]:
        if not row_number < self.height:
            raise IndexError()
        for x in range(self.width):
            yield self.get_item_with_cord(x, row_number)

    def iterate_over_column(self, column_number: int) -> Iterable[T]:
        if not column_number < self.width:
            raise IndexError()
        for y in range(self.height):
            yield self.get_item_with_cord(column_number, y)

    def in_borders(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def point_in_borders(self, point: Point) -> bool:
        return self.in_borders(point.x, point.y)

    def set_item_with_cord(self, x: int, y: int, value: T) -> NoReturn:
        if not self.in_borders(x, y):
            raise IndexError()
        self._matrix[x][y] = value

    def set_item_with_point(self, point: Point, value: T) -> NoReturn:
        self.set_item_with_cord(point.x, point.y, value)

    def get_item_with_cord(self, x: int, y: int) -> T:
        if not self.in_borders(x, y):
            raise IndexError()
        return self._matrix[x][y]

    def get_item_with_point(self, point: Point) -> T:
        return self.get_item_with_cord(point.x, point.y)

    def __contains__(self, item: Point) -> bool:
        return self.point_in_borders(item)

    def __getitem__(self, key: Point) -> T:
        if not self.in_borders(key.x, key.y):
            raise IndexError()
        return self._matrix[key.x][key.y]

    def __setitem__(self, key: Point, value: T) -> NoReturn:
        self.set_item_with_point(key, value)
