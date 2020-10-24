from typing import Iterable, Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')
def fold_left(function: Callable[[B, A], B], initializer: B, iterable: Iterable[A]) -> B:
    for value in iterable:
        initializer = function(initializer, value)
    return initializer