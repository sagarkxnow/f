from f import Maybe, Nothing


def test() -> Maybe[str]:
	return Maybe.pure(1) | (lambda a: a.lower())