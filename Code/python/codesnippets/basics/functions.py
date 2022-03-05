# Basic Functions
num = -4.745
num1 = pow(4, 2)                # Or: 4** 2
num = abs(num)                       # <float> = abs(<complex>)
num = round(<num> [, ±ndigits])        # `round(126, -1) == 130`

# Math
from math import e, pi, inf, nan, isinf, isnan
from math import sin, cos, tan, asin, acos, atan, degrees, radians
from math import log, log10, log2


# Statistics
from statistics import mean, median, variance, stdev, quantiles, groupby

# Random
from random import random, randint, choice, shuffle, gauss, seed

random_floats = random()                       # A float inside [0, 1).
random_ints   = randint(from_inc, to_inc)      # An int inside [from_inc, to_inc].
<el>    = choice(<sequence>)             # Keeps the sequence intact.


# Combinatorics
# Every function returns an iterator.
# If you want to print the iterator, you need to pass it to the list() function first!
from itertools import product, combinations, combinations_with_replacement, permutations

product([0, 1], repeat=3)
# OUTPUT :: [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), ..., (1, 1, 1)]

product('abc', 'abc')                                    #   a  b  c
# OUTPUT :: [('a', 'a'), ('a', 'b'), ('a', 'c'),         # a x  x  x
#  ('b', 'a'), ('b', 'b'), ('b', 'c'),                   # b x  x  x
#  ('c', 'a'), ('c', 'b'), ('c', 'c')]                   # c x  x  x

combinations('abc', 2)                                   #   a  b  c
# OUTPUT :: [('a', 'b'), ('a', 'c'),                     # a .  x  x
#  ('b', 'c')]                                           # b .  .  x

combinations_with_replacement('abc', 2)                  #   a  b  c
# OUTPUT :: [('a', 'a'), ('a', 'b'), ('a', 'c'),         # a x  x  x
#  ('b', 'b'), ('b', 'c'),                               # b .  x  x
#  ('c', 'c')]                                           # c .  .  x

permutations('abc', 2)                                   #   a  b  c
# [('a', 'b'), ('a', 'c'),                               # a .  x  x
#  ('b', 'a'), ('b', 'c'),                               # b x  .  x
#  ('c', 'a'), ('c', 'b')]                               # c x  x  .