from copy import deepcopy
from typing import Sequence, TypeAlias

from vector2 import Vector2

Vector2Like: TypeAlias = Vector2 | Sequence[int | float]
Rotations: TypeAlias = list[list[Vector2Like]]


class Tetromino:
    def __init__(self, char: str, rotations: Rotations, rotation_index: int = 0, pos: Vector2Like = (0, 0)) -> None:
        self.char: str = char
        self.rotations: Rotations = [[Vector2(block) for block in rotation] for rotation in rotations]
        self.rotation_index: int = rotation_index
        self.rotation: list[Vector2] = self.rotations[self.rotation_index]
        self.pos: Vector2 = Vector2(pos)

    @property
    def rotation_index(self) -> int:
        return self._rotation_index

    @rotation_index.setter
    def rotation_index(self, value: int) -> None:
        self._rotation_index = value % len(self.rotations)
        self.rotation = self.rotations[self._rotation_index]

    def rotate(self) -> 'Tetromino':
        self.rotation_index += 1
        return self

    def move(self, dx: int, dy: int) -> 'Tetromino':
        self.pos += Vector2(dx, dy)
        return self

    def clone(self) -> 'Tetromino':
        return deepcopy(self)

    def get_margins(self) -> dict[str, int]:
        xs = [b.x for b in self.rotation]
        ys = [b.y for b in self.rotation]
        return {'x_min': int(min(xs)), 'x_max': int(max(xs)),
                'y_min': int(min(ys)), 'y_max': int(max(ys))}
