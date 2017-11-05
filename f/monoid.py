from typing import TypeVar, Generic, Sequence  # pylint: disable = W0611
from abc import ABC, abstractstaticmethod, abstractmethod

M = TypeVar('M')
T = TypeVar('T')


def append(first: 'Monoid[M]', second: 'Monoid[M]'):
    return first + second


def concat(m: 'Monoid[M]', ms: 'Sequence[Monoid[M]]') -> 'Monoid[M]':
    return m @ ms


class Monoid(ABC, Generic[M]):
    @staticmethod
    @abstractstaticmethod
    def empty():
        raise NotImplementedError()

    @abstractmethod
    def append(self, m):
        raise NotImplementedError()

    @abstractmethod
    def concat(self, ms):
        raise NotImplementedError()

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError()

    @abstractmethod
    def __matmul__(self, other):
        raise NotImplementedError()
