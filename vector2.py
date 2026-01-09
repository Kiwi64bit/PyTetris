from typing import Any, Iterator, Sequence, TypeAlias

number: TypeAlias = int | float

class Vector2:
    def __init__(self, x: number | Sequence[number] = 0.0, y: number = 0.0) -> None:
        if isinstance(x, (Sequence | Vector2)):
            self.x, self.y = float(x[0]), float(x[1])
        else:
            self.x = float(x)
            self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: number) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: number) -> 'Vector2':
        return self * scalar

    def __truediv__(self, scalar: number) -> 'Vector2':
        return Vector2(self.x / scalar, self.y / scalar)

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Vector2) and self.x == other.x and self.y == other.y

    def __iter__(self) -> Iterator[number]:
        yield self.x
        yield self.y

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
