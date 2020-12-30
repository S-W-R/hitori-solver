from entities.cell_type import CellType
from puzzle.puzzle import Puzzle
from puzzle.puzzle_state import PuzzleState
from puzzle_checker.puzzle_checker import PuzzleChecker


class PuzzleSolver:
    def __init__(self):
        self._puzzle_checker = PuzzleChecker()

    def solve_puzzle(self, puzzle: Puzzle) -> Puzzle:
        if self._puzzle_checker.puzzle_solved(puzzle):
            puzzle.puzzle_state = PuzzleState.SOLVED
            return puzzle
        if self._puzzle_checker.puzzle_unsolvable(puzzle):
            puzzle.puzzle_state = PuzzleState.UNSOLVABLE
            return puzzle
        conflicts = list(self._puzzle_checker.find_line_conflicts(puzzle))
        if len(conflicts) == 0:
            raise Exception('unknown error')
        conflict = conflicts[0]
        for point in conflict.points:
            new_puzzle = puzzle.clone_puzzle()
            for point_to_delete in conflict.points:
                if point_to_delete == point:
                    continue
                cell = new_puzzle.game_field[point_to_delete]
                cell.cell_type = CellType.DELETED
            solution = self.solve_puzzle(new_puzzle)
            if solution.puzzle_state == PuzzleState.SOLVED:
                return solution
        puzzle.puzzle_state = PuzzleState.UNSOLVABLE
        return puzzle
