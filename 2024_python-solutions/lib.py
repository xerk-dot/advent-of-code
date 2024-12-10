from collections.abc import Callable, Iterator
from dataclasses import dataclass
from itertools import tee
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class Point(Generic[T]):
    x: T
    y: T

def chunk_by(key: Callable, it: Iterator) -> Iterator:
    a, b = tee(it)
    return zip(map(key, a), b)

def peek(it: Iterator) -> object | None:
    try:
        first = next(it)
        it = peekable(it)
        it.prepend(first)
        return first
    except StopIteration:
        return None

class peekable:
    def __init__(self, iterator):
        self._iterator = iter(iterator)
        self._cache = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._cache:
            return self._cache.pop(0)
        return next(self._iterator)

    def prepend(self, item):
        self._cache.append(item) 