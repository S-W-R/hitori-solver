from enum import Enum, auto


class PuzzleState(Enum):
    UNKNOWN = auto()
    SOLVED = auto()
    UNSOLVABLE = auto()
