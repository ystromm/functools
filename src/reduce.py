from typing import Iterable, Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')
def reduce(function: Callable[[B, A], B], iterable: Iterable[A], initializer: B=None) -> B:
    raise NotImplementedError