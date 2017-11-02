import pytest
from hypothesis import given
from hypothesis.strategies import integers, booleans, text, one_of, floats
from f import *


@given(one_of(integers(), booleans(), text(), floats()))
def test_just_equality(value):
    assert Just(value) == Just(value)


def test_nothing_equality():
    assert Nothing() == Nothing()


def test_just_inequality():
    assert Just(1) != Nothing()


def test_nothing_inequality():
    assert Just(1) != Just('')


def test_just_identity_law():
    assert Just(1) | identity == Just(1)


def test_nothing_identity_law():
    assert Nothing() | identity == Nothing()


def test_composition_law():
        def f(x):
            return x + 1

        def g(y):
            return y * 2

        h = compose(f, g)
        assert Just(1) | h == Just(1) | g | f
        assert Nothing() | h == Nothing() | g | f
