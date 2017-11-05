from f import Maybe, Nothing


def test_just() -> Maybe[int]:
	return Maybe.pure(1) >> (lambda a: Maybe.pure(1))


def test_nothing() -> Maybe[int]:
	return Maybe.pure(1) >> (lambda a: Nothing())
