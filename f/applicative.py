from abc import ABC, abstractstaticmethod, abstractmethod
from f.functor import Functor


class Applicative(Functor, ABC):
    @abstractstaticmethod
    def pure(value):
        raise NotImplementedError()

    @abstractmethod
    def apply(self, f):
        raise NotImplementedError()

    def __mul__(self, f):
        return self.apply(f)
