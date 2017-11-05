from f import Maybe


def test_just() -> Maybe[str]:
    return Maybe.pure(1) >> (lambda a: str(a))
