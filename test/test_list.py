from f import List, identity, compose
from hypothesis.strategies import assume, integers, lists as lists_
from hypothesis import given, settings
from .strategies import anything, unaries, lists
from .monad_test import MonadTest
from .monoid_test import MonoidTest


class TestList(MonadTest, MonoidTest):
    @given(lists())
    def test_left_append_identity_law(self, l):
        assert List.empty() + l == l

    @given(lists_(anything()), integers(min_value=0))
    def test_getitem(self, l, index):
        assume(index < len(l))
        assert l[index] == l[index]

    @given(lists())
    def test_right_append_identity_law(self, l):
        assert l + List.empty() == l

    @given(lists(), lists([lists()]))
    def test_concat(self, l, ls):
        assert l @ ls == List(l.values + tuple(v for l in ls for v in l))

    @given(lists(), lists(), lists())
    def test_append_associativity_law(self, x, y, z):
        assert (x + y) + z == x + (y + z)

    @settings(deadline=None)
    @given(lists(), unaries(lists()), unaries(lists()))
    def test_associativity_law(self, l, f, g):
        assert (l >> f) >> g == l >> (lambda x: f(x) >> g)

    @given(lists_(anything()))
    def test_equality(self, t):
        assert List(t) == List(t)

    @given(unaries(), unaries(), lists())
    def test_composition_law(self, f, g, l):
        h = compose(f, g)
        assert l | h == l | g | f

    @given(lists())
    def test_identity_law(self, l):
        assert l | identity == l

    @given(lists_(anything()), lists_(anything()))
    def test_inequality(self, first, second):
        assume(first != second)
        assert List(first) != List(second)

    @given(anything(), unaries(lists()))
    def test_left_identity_law(self, v, f):
        assert List.pure(v) >> f == f(v)

    @given(lists())
    def test_right_identity_law(self, l):
        assert l >> List.pure == l

    @given(lists_(anything()), anything())
    def test_in(self, l, v):
        assume(v in l)
        assert v in List(l)

    @given(lists_(anything()))
    def test_reverse(self, l):
        assert List(l).reverse == List(reversed(l))

    @given(lists_(anything()))
    def test_head(self, l):
        assert List(l).head == (l[0] if l else None)

    @given(lists_(anything()))
    def test_tail(self, l):
        assert List(l).tail == List(l[1:])

    @given(lists_(anything()))
    def test_filter(self, l):
        def p(v):
            return id(v) % 2 == 0

        assert List(l).filter(p) == List(filter(p, l))

    @given(lists_(integers()), integers())
    def test_reduce(self, l, i):
        assume(sum(l) == i)
        assert List(l).reduce(lambda a, b: a + b, 0) == i
