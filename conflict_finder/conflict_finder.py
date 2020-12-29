from collections import Iterable

from conflict_finder.conflicts import LineConflict
from entities.cell_type import CellType
from misc.singleton import Singleton
from puzzle.puzzle import Puzzle


class ConflictFinder(metaclass=Singleton):
    def __init__(self):
        pass

    def find_line_conflicts(self, puzzle: Puzzle) -> Iterable[LineConflict]:
        line_conflicts = []
        for x in range(puzzle.width):
            known_values = dict()  # Dict[int, List[Point]]
            for y in range(puzzle.height):
                cell = puzzle.game_field.get_item_with_cord(x, y)
                if cell.cell_type != CellType.NUMBER:
                    continue
                value = cell.value
                if value in known_values:
                    known_values[value].append(cell.position)
                else:
                    known_values[value] = [cell.position]
            for positions in known_values.values():
                if len(positions) > 1:
                    line_conflicts.append(LineConflict(positions))

        for y in range(puzzle.height):
            known_values = dict()  # Dict[int, List[Point]]
            for x in range(puzzle.width):
                cell = puzzle.game_field.get_item_with_cord(x, y)
                if cell.cell_type != CellType.NUMBER:
                    continue
                value = cell.value
                if value in known_values:
                    known_values[value].append(cell.position)
                else:
                    known_values[value] = [cell.position]
            for positions in known_values.values():
                if len(positions) > 1:
                    line_conflicts.append(LineConflict(positions))

        return line_conflicts

    def contains_near_deleted(self) -> bool:

