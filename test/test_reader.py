from .monad_test import MonadTest
from .strategies import anything, unaries, readers
from hypothesis import given, assume
from f import Reader, identity, compose


class TestReader(MonadTest):
    @given(anything(), anything())
    def test_right_identity_law(self, value, context):
        assert ((Reader.pure(value) >> Reader.pure)(context) ==
                Reader.pure(value)(context))

    @given(unaries(readers()), anything(), anything())
    def test_left_identity_law(self, f, value, context):
        assert (Reader.pure(value) >> f)(context) == f(value)(context)

    @given(readers(), unaries(readers()), unaries(readers()), anything())
    def test_associativity_law(self, reader, f, g, context):
        assert (((reader >> f) >> g)(context) ==
                (reader >> (lambda x: f(x) >> g))(context))

    @given(anything(), anything())
    def test_equality(self, value, context):
        assert Reader.pure(value)(context) == Reader.pure(value)(context)

    @given(anything(), anything(), anything())
    def test_inequality(self, first, second, context):
        assume(first != second)
        assert Reader.pure(first)(context) != Reader.pure(second)(context)

    @given(anything(), anything())
    def test_identity_law(self, value, context):
        assert ((Reader.pure(value) | identity)(context) ==
                Reader.pure(value)(context))

    @given(unaries(), unaries(), anything(), anything())
    def test_composition_law(self, f, g, value, context):
        h = compose(f, g)
        assert ((Reader.pure(value) | h)(context) ==
                (Reader.pure(value) | g | f)(context))
