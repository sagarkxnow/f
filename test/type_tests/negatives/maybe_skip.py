from f import Maybe, Nothing


def test_just() -> Maybe[int]:
	return Maybe.pure('test') & Maybe.pure('')
