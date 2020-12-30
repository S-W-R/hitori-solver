import argparse
from typing import Iterable

from puzzle_parser.puzzle_parser import PuzzleParser
from puzzle_solver.puzzle_solver import PuzzleSolver
from ui.console_ui import ConsoleUi


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('width',
                        action='store',
                        type=int,
                        help='width')
    parser.add_argument('height',
                        action='store',
                        type=int,
                        help='height')
    return parser


def read_game_field(width: int, height: int) -> Iterable[str]:
    for i in range(height):
        line = input()
        if len(line) != width:
            raise AttributeError('incorrect input')
        yield line


def main():
    console_ui = ConsoleUi()
    parser = init_parser()
    args = parser.parse_args()
    width = args.width
    height = args.height
    if width <= 0 or height <= 0:
        raise AttributeError('incorrect width or height')
    print('write puzzle matrix:')
    lines = list(read_game_field(width, height))
    puzzle_parser = PuzzleParser()
    puzzle = puzzle_parser.parse_from_lines_with_size(width=width,
                                                      height=height,
                                                      lines=lines)

    print()
    print('initial puzzle:')
    console_ui.print_puzzle(puzzle)
    puzzle_solver = PuzzleSolver()
    solved_puzzle = puzzle_solver.solve_puzzle(puzzle)
    print()
    console_ui.print_solution(solved_puzzle)


if __name__ == '__main__':
    main()
