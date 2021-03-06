from copy import copy
from typing import Iterable, NoReturn

from const.rules import NEAR_POSITION
from entities.cell import Cell
from geometry.matrix import Matrix
from geometry.point import Point
from puzzle.puzzle_state import PuzzleState


class Puzzle:
    def __init__(self, game_field: Matrix[Cell]):
        self._game_field = game_field
        self._puzzle_state = PuzzleState.UNKNOWN

    @property
    def puzzle_state(self) -> PuzzleState:
        return self._puzzle_state

    @puzzle_state.setter
    def puzzle_state(self, value: PuzzleState) -> NoReturn:
        self._puzzle_state = value

    @property
    def width(self) -> int:
        return self._game_field.width

    @property
    def height(self) -> int:
        return self._game_field.height

    @property
    def game_field(self) -> Matrix[Cell]:
        return self._game_field

    def point_in_game_field(self, point: Point) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def get_near_points_with_point(self, point: Point) -> Iterable[Point]:
        for near_pos in NEAR_POSITION:
            new_point = point + near_pos
            if self.point_in_game_field(new_point):
                yield new_point

    def get_near_points_with_cord(self, x, y) -> Iterable[Point]:
        return self.get_near_points_with_point(Point(x, y))

    def clone_puzzle(self) -> 'Puzzle':
        new_matrix = Matrix(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                old_cell = self._game_field.get_item_with_cord(x, y)
                new_cell = copy(old_cell)
                new_matrix.set_item_with_cord(x, y, new_cell)
        return Puzzle(new_matrix)
