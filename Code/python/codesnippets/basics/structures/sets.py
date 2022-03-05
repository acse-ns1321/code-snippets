

# Initialize
set_a = {1, 2, 3}                                # initialize manually
set_b = set(range(5))                            # initialize from iteratable

# Add elements
set_a.add(13)                                    # add new element to set
set_a.update([21, 22, 23])                       # update set with elements from iterable

# Delete Elements
set_a.discard(13)                                # discard element from set
set_a.pop()                                      # remove and return an arbitrary set element

# Check if element is present
2 in {1, 2, 3}                               # true if 2 in set
5 not in {1, 2, 3}                           # true if 5 not in set

# Subset
set_a.issubset(set_b)                                # test whether every element in a is in b
set_a <= set_b                                       # issubset in operator form
# Superset
set_a.issuperset(set_b)                              # test whether every element in b is in a
set_a >= set_b                                      # issuperset in operator form
# Intersection and Union
set_a.intersection(set_b)                            # return the intersection of two sets as a new set
set_a.union(set_b)                                   # return the union of sets as a new set
# Difference in Sets
set_a.difference(set_b)                              # return the difference of two or more sets as a new set
set_a - set_b                                       # difference in operator form
set_a.symmetric_difference(set_b)                    # return the symmetric difference of two sets as a new set

# Frozen Set
# Is immutable and hashable.
# That means it can be used as a key in a dictionary or as an element in a set.
c = frozenset()                              # the same as set but immutable
