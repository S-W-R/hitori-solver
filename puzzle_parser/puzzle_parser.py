from typing import List

from entities.cell import Cell
from entities.cell_type import CellType
from geometry.matrix import Matrix
from geometry.point import Point
from misc.singleton import Singleton
from puzzle.puzzle import Puzzle


class PuzzleParser(metaclass=Singleton):
    def __init__(self):
        pass

    def parse_from_lines_with_size(self, width: int, height: int,
                                   lines: List[str]) -> Puzzle:
        game_field = Matrix(width, height)
        if len(lines) != height:
            raise AttributeError('incorrect height')
        for y in range(height):
            line = lines[y]
            if len(line) != width:
                raise AttributeError('incorrect width')
            for x in range(width):
                char = line[x]
                pos = Point(x, y)
                cell = self._cell_from_symbol(pos, char)
                game_field[pos] = cell
        return Puzzle(game_field)

    def _cell_from_symbol(self, pos: Point, char: str) -> Cell:
        if char == ' ':
            return Cell(position=pos, cell_type=CellType.DELETED, value=-1)
        elif char.isdigit():
            return Cell(position=pos, cell_type=CellType.NUMBER,
                        value=int(char))
        else:
            raise AttributeError('unknown symbol')
