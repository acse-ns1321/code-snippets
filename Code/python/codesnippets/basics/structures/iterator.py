iter_variable = iter(<collection>)                 # `iter(iter_variable)` returns unmodified iterator.
iter_variable = iter(<function>, to_exclusive)     # A sequence of return values until 'to_exclusive'.
<el>   = next(iter_variable [, default])           # Raises StopIteration or returns 'default' on end.
<list> = list(iter_variable)                       # Returns a list of iterator's remaining elements.



from itertools import count, repeat, cycle, chain, islice
iter_variable = count(start=0, step=1)             # Returns updated value endlessly. Accepts floats.
iter_variable = repeat(<el> [, times])             # Returns element endlessly or 'times' times.
iter_variable = cycle(<collection>)                # Repeats the sequence endlessly.
iter_variable = chain(<coll_1>, <coll_2> [, ...])  # Empties collections in order.
iter_variable = chain.from_iterable(<collection>)  # Empties collections inside a collection in order.
iter_variable = islice(<coll>, to_exclusive)       # Only returns first 'to_exclusive' elements.
iter_variable = islice(<coll>, from_inclusive, …)  # `to_exclusive, step_size`.

from collections.abc import Iterable, Collection, Sequence
isinstance([1, 2, 3], Iterable)
# Output:: True
# +------------------+------------+------------+------------+
# |                  |  Iterable  | Collection |  Sequence  |
# +------------------+------------+------------+------------+
# | list, range, str |    yes     |    yes     |    yes     |
# | dict, set        |    yes     |    yes     |            |
# | iter             |    yes     |            |            |
# +------------------+------------+------------+------------+