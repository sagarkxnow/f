from typing import TypeVar, Callable, Iterator, Tuple, Generic, Set, Collection, Iterable
from functools import reduce
from f.monoid import Monoid
from f.monad import Monad
from .util import Unary, Predicate

A = TypeVar('A')
B = TypeVar('B')


class List(Monad, Monoid[A], Generic[A], Collection[A], Iterable[A]):
    @staticmethod
    def empty() -> 'List[A]':
        t = set()  # type: Set[A]
        return List(v for v in t)

    @staticmethod
    def pure(value: A) -> 'List[A]':
        return List(i for i in (value,))

    def __or__(self, f: Unary[A, B]) -> 'List[B]':
        return self.map(f)

    def append(self, m: 'List[A]') -> 'List[A]':
        return List(v for v in self.values + m.values)

    def __contains__(self, x) -> bool:
        return x in self.values

    def __add__(self, other: 'List[A]') -> 'List[A]':
        return self.append(other)

    def __len__(self) -> int:
        return len(self.values)

    def __iter__(self) -> Iterator[A]:
        return iter(self.values)

    def bind(self, f: 'Unary[A, List[B]]') -> 'List[B]':
        return self.reduce(lambda l, v: l + f(v), List.empty())

    def skip(self, n: 'List[B]') -> 'List[B]':
        return self.bind(lambda _: n)

    def __and__(self, n: 'List[B]') -> 'List[B]':
        return self.skip(n)

    def __rshift__(self, f: 'Unary[A, List[B]]') -> 'List[B]':
        return self.bind(f)

    def __getitem__(self, item):
        return self.values[item]

    @property
    def reverse(self) -> 'List[A]':
        return List(reversed(self.values))

    def filter(self, p: Predicate[A]) -> 'List[A]':
        return List(filter(p, self.values))

    def reduce(self, f: Callable[[B, A], B], initial: B) -> B:
        return reduce(f, self.values, initial)

    @property
    def head(self) -> A:
        return self.values[0] if self.values else None

    def __reversed__(self) -> 'List[A]':
        return self.reverse

    @property
    def tail(self) -> 'List[A]':
        return List(i for i in self.values[1:])

    def map(self, f: Unary[A, B]) -> 'List[B]':
        mapped = map(f, self.values)
        return List(mapped)

    def __init__(self, values: Iterator[A]) -> None:
        self._values = tuple(values)

    def concat(self, ms: 'List[List[A]]') -> 'List[A]':
        return ms.reduce(lambda a, l: a + l, self)

    def __matmul__(self, other: 'List[List[A]]') -> 'List[A]':
        return self.concat(other)

    def __eq__(self, other) -> bool:
        return isinstance(other, List) and self.values == other.values

    @property
    def values(self) -> Tuple[A, ...]:
        return self._values

    def __repr__(self) -> str:
        return '[' + ', '.join(repr(v) for v in self.values) + "]"
