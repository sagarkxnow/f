from f import Maybe, Nothing


def test_just() -> Maybe[str]:
	return Maybe.pure('test') | (lambda a: a.lower())


def test_nothing() -> Maybe[str]:
	return Nothing() | (lambda a: a.lower())
