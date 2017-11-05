from f import Maybe, Nothing


def test_just() -> Maybe[int]:
	return Maybe.pure(1) >> (lambda a: Maybe.pure(''))
