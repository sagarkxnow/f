from f import Maybe, Nothing


def test_just() -> Maybe[str]:
    return Maybe.pure(1) >> (lambda a: Maybe.pure(str(a)))


def test_nothing() -> Maybe[str]:
    return Nothing() >> (lambda a: Maybe.pure(a + 'test'))
