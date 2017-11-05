from typing import TypeVar, Generic, Type
from f.monad import Monad
from .util import identity, Unary, compose

V = TypeVar('V')
C = TypeVar('C')
N = TypeVar('N')


class Reader(Monad,
             Generic[C, V]):
    def __init__(self, f: Unary[C, V]) -> None:
        self._f = f

    @staticmethod
    def pure(value: V) -> 'Reader[C, V]':
        return Reader(lambda _: value)

    @staticmethod
    def ask(_: Type[C]) -> 'Reader[C, C]':
        # Without the type parameter, mypy can't do inference
        # in client code
        return Reader(identity)

    def __call__(self, w: C) -> V:
        return self._f(w)

    def bind(self, f: 'Unary[V, Reader[C, N]]') -> 'Reader[C, N]':
        return Reader(lambda w: f(self(w))(w))

    # todo: find a way to move this to Functor without breaking client
    # type inference
    def __or__(self, f: Unary[V, N]) -> 'Reader[C, N]':
        return self.map(f)

    def map(self, f: Unary[V, N]) -> 'Reader[C, N]':
        return Reader(compose(f, self._f))

    # todo: find a way to move this to Monad without breaking client
    # type inference
    def skip(self, n: 'Reader[C, N]') -> 'Reader[C, N]':
        return self.bind(lambda _: n)

    def __and__(self, n: 'Reader[C, N]') -> 'Reader[C, N]':
        return self.skip(n)

    # todo: find a way to move this to Monad without breaking client type
    # inference
    def __rshift__(self, f: 'Unary[V, Reader[C, N]]') -> 'Reader[C, N]':
        return self.bind(f)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Reader) and
                self._f.__code__.co_code == other._f.__code__.co_code)
