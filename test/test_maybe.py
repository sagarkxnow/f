from typing import Any
from hypothesis import assume, given
from f import Maybe, Just, Nothing, Unary, identity, compose
from .monad_test import MonadTest
from .strategies import anything, unaries, maybes


class TestMaybe(MonadTest):
    def test_equality(self):
        self._test_just_equality()
        self._test_nothing_equality()

    def test_inequality(self):
        self._test_just_inequality()
        self._test_nothing_inequality()

    def test_identity_law(self):
        self._test_just_identity_law()
        self._test_nothing_identity_law()

    @given(maybes())
    def test_right_identity_law(self, maybe: Maybe):
        assert maybe >> Maybe.pure == maybe

    @given(anything(), unaries(maybes()))
    def test_left_identity_law(self, value, f: Unary[Any, Maybe]):
        assert Maybe.pure(value) >> f == f(value)

    @given(maybes(), unaries(maybes()), unaries(maybes()))
    def test_associativity_law(self,
                               maybe: Maybe,
                               f: Unary[Any, Maybe],
                               g: Unary[Any, Maybe]):
        assert (maybe >> f) >> g == maybe >> (lambda x: f(x) >> g)

    @given(anything())
    def _test_just_equality(self, value):
        assert Just(value) == Just(value)

    def _test_nothing_equality(self):
        assert Nothing() == Nothing()

    @given(anything())
    def _test_just_inequality(self, value):
        assert Just(value) != Nothing()

    @given(anything(), anything())
    def _test_nothing_inequality(self, first, second):
        assume(first != second)
        assert Just(first) != Just(second)

    @given(anything())
    def _test_just_identity_law(self, value):
        assert Just(value) | identity == Just(value)

    def _test_nothing_identity_law(self):
        assert Nothing() | identity == Nothing()

    @given(unaries(), unaries(), anything())
    def test_composition_law(self, f: Unary, g: Unary, value):
        h = compose(f, g)
        assert Just(value) | h == Just(value) | g | f
        assert Nothing() | h == Nothing() | g | f
