# Tuple is an immutable and hashable list.
tup= ()
tup = ("el",)                           # Or: <el>,
tup = ("<el_1>", "<el_2>" [:, "..."])          # Or: <el_1>, <el_2> [, ...]

# Named Tuple
# Tuple's subclass with named elements.
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, y=2)
# Output :: Point(x=1, y=2)
p[0]
# Output ::1
p.x
# Output ::1
getattr(p, 'y')
# Output ::2
p._fields  # Or: Point._fields
# Output ::('x', 'y')