from enum import Enum, auto


class ConflictType(Enum):
    MORE_THAN_ONE_IN_LINE = auto()
    DELETED_NEAR = auto()
    CELLS_NOT_CONNECTED = auto()
