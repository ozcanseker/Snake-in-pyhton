from enum import Enum


class GameInput(Enum):
    QUIT = "QUIT"


class MovementInput(Enum):
    LEFT = "LEFT"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    RIGHT = "RIGHT"
