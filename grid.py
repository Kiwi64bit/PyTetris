from copy import deepcopy
from typing import Any


class Grid:
    def __init__(self, width: int, height: int, default: Any = None) -> None:
        self.width: int = width
        self.height: int = height
        self.default: Any = default
        self.data: list[list[Any]] = [[self.default] * width for _ in range(self.height)]

    def set(self, x: int, y: int, value: Any) -> None:
        x, y = int(x), int(y)
        if not self.is_inside(x, y):
            return
        self.data[y][x] = value

    def get(self, x: int, y: int) -> Any:
        if not self.is_inside(x, y):
            return None
        x, y = int(x), int(y)
        return self.data[y][x]

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_empty(self, x: int, y: int) -> bool:
        return self.get(x, y) == self.default

    def fill(self, value: Any) -> None:
        for y in range(self.height):
            self.data[y] = [value] * self.width

    def reset(self) -> None:
        self.fill(self.default)

    def clone(self) -> 'Grid':
        return deepcopy(self)

    def __str__(self) -> str:
        rows: list[str] = [' '.join(str(cell) for cell in row) for row in self.data]
        grid_str: str = '\n'.join(rows)
        return grid_str


if __name__ == '__main__':
    grid: Grid = Grid(10, 20, '.')
    grid.set(5, 5, '#')
    grid.set(5, 3, '#')
    grid.set(5, 2, '#')
    print(grid)
