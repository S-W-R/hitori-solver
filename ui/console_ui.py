from entities.cell_type import CellType
from misc.singleton import Singleton
from puzzle.puzzle import Puzzle
from puzzle.puzzle_state import PuzzleState


class ConsoleUi(metaclass=Singleton):
    def __init__(self):
        pass

    def print_puzzle(self, puzzle: Puzzle):
        border = f'+{"-" * puzzle.width}+'
        print(border)
        for y in range(puzzle.height):
            line = '|'
            for x in range(puzzle.width):
                cell = puzzle.game_field.get_item_with_cord(x, y)
                if cell.cell_type == CellType.DELETED:
                    line += ' '
                elif cell.cell_type == CellType.DISABLED:
                    line += '+'
                elif cell.cell_type == CellType.NUMBER:
                    line += str(cell.value)
                else:
                    raise AttributeError('unknown cell type')
            line += '|'
            print(line)
        print(border)

    def print_solution(self, puzzle: Puzzle):
        if puzzle.puzzle_state == PuzzleState.UNSOLVABLE:
            print('puzzle is unsolvable')
        elif puzzle.puzzle_state == PuzzleState.SOLVED:
            print('solution: ')
            self.print_puzzle(puzzle)
        else:
            raise AttributeError('unknown puzzle state')
