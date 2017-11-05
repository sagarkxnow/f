from f import Maybe, Nothing, identity


def test_just() -> Maybe[int]:
	return Maybe.pure(1) | (lambda a: str(a))
