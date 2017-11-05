from abc import ABC, abstractstaticmethod, abstractmethod


class Monad(ABC):
    # todo: improve typing here
    @staticmethod
    @abstractstaticmethod
    def pure(value):
        raise NotImplementedError()

    @abstractmethod
    def bind(self, f):
        raise NotImplementedError()

    @abstractmethod
    def skip(self, n):
        return self.bind(lambda _: n)

    @abstractmethod
    def __and__(self, n):
        return self.skip(n)

    @abstractmethod
    def __rshift__(self, f):
        raise NotImplementedError()
