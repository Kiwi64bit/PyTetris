from copy import deepcopy
from random import sample
from typing import Any, Sequence


class RandomBag:
    def __init__(self, items: Sequence[Any]) -> None:
        self.items: Sequence[Any] = deepcopy(items)
        self.bag: list[Any] = []

    def next(self) -> Any:
        if self.is_bag_empty():
            self.reset_bag()
        return self.bag.pop()

    def is_bag_empty(self) -> bool:
        return not self.bag

    def reset_bag(self) -> None:
        self.bag = sample(deepcopy(self.items), k=len(self.items))
