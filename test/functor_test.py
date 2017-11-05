from abc import ABC, abstractmethod


class FunctorTest(ABC):

    @abstractmethod
    def test_equality(self):
        raise NotImplementedError()

    @abstractmethod
    def test_inequality(self):
        raise NotImplementedError()

    @abstractmethod
    def test_identity_law(self):
        raise NotImplementedError()

    @abstractmethod
    def test_composition_law(self):
        raise NotImplementedError()
