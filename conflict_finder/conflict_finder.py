from collections import deque
from typing import Set, Iterable

from conflict_finder.LineConflict import LineConflict
from entities.cell_type import CellType
from geometry.point import Point
from misc.singleton import Singleton
from puzzle.puzzle import Puzzle


class ConflictFinder(metaclass=Singleton):
    def __init__(self):
        pass

    def puzzle_solved(self, puzzle: Puzzle) -> bool:
        return ((not self.contains_near_deleted(puzzle))
                and self.cells_connected(puzzle)
                and len(list(self.find_line_conflicts(puzzle))) == 0)

    def puzzle_unsolvable(self, puzzle: Puzzle) -> bool:
        return (self.contains_near_deleted(puzzle)
                or not self.cells_connected(puzzle))

    def find_line_conflicts(self, puzzle: Puzzle) -> Iterable[LineConflict]:
        line_conflicts = []
        for x in range(puzzle.width):
            known_values = dict()
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
            known_values = dict()
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

    def contains_near_deleted(self, puzzle: Puzzle) -> bool:
        game_matrix = puzzle.game_field
        for x in range(puzzle.width):
            for y in range(puzzle.height):
                point = Point(x, y)
                cell = game_matrix[point]
                if cell.cell_type == CellType.DELETED:
                    for near_point in puzzle.get_near_points_with_point(point):
                        near_cell = game_matrix[point + near_point]
                        if near_cell.cell_type == CellType.DELETED:
                            return True
        return False

    def cells_connected(self, puzzle: Puzzle) -> bool:
        number_points = set()  # type: Set[Point]
        number_point = None  # type: Point
        game_matrix = puzzle.game_field
        for x in range(puzzle.width):
            for y in range(puzzle.height):
                point = Point(x, y)
                if game_matrix[point].cell_type == CellType.NUMBER:
                    number_point = point
                    number_points.add(point)
        if len(number_points) == 0:
            return True
        current_group = set()  # type:  Set[Point]
        frontier = deque()
        frontier.append(number_point)
        while len(frontier) > 0:
            current = frontier.popleft()
            current_group.add(current)
            for near_pos in puzzle.get_near_points_with_point(current):
                near_cell = game_matrix[near_pos]
                if (near_cell.cell_type != CellType.NUMBER
                        or near_pos in current_group):
                    continue
                frontier.append(near_pos)
                current_group.add(near_pos)
        for point in number_points:
            if point not in current_group:
                return False
        return True
