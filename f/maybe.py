from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from f.functor import Functor
from f.monad import Monad
from .util import Unary

V = TypeVar('V')
N = TypeVar('N')


class Maybe(Monad, Generic[V], Functor[V], ABC):

    @classmethod
    def pure(cls, value: V) -> 'Maybe[V]':
        return Just(value)

    @abstractmethod
    def bind(self, f: 'Unary[V, Maybe[N]]') -> 'Maybe[N]':
        raise NotImplementedError()

    def __rshift__(self, f: 'Unary[V, Maybe[N]]') -> 'Maybe[N]':
        return self.bind(f)


    def skip(self, n: 'Maybe[N]') -> 'Maybe[N]':
        return n

    def __or__(self, f: Unary[V, N]) -> 'Maybe[N]':
        return self.map(f)

    def __and__(self, n: 'Maybe[N]') -> 'Maybe[N]':
        return self.skip(n)

    @abstractmethod
    def map(self, f: Unary[V, N]) -> 'Maybe[N]':
        raise NotImplementedError()

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__


class Just(Maybe[V], Generic[V]):
    def __init__(self, value: V) -> None:
        self._value = value

    @property
    def value(self) -> V:
        return self._value

    def bind(self, f: Unary[V, Maybe[N]]) -> Maybe[N]:
        return f(self.value)

    def map(self, f: Unary[V, N]) -> Maybe[N]:
        return Just(f(self.value))

    def __repr__(self) -> str:
        return 'Just({})'.format(self.value)


class Nothing(Maybe):

    def bind(self, _) -> Maybe:
        return self 

    def map(self, _) -> Maybe:
        return Nothing()

    def __repr__(self):
        return "Nothing"


