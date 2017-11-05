from functools import partial
from .functor import Functor
from .monad import Monad
from .list import List
from .monoid import Monoid
from .maybe import Just, Nothing, Maybe
from .reader import Reader
from .util import (identity,
                   compose,
                   Immutable,
                   Unary,
                   Predicate,
                   has_type)
