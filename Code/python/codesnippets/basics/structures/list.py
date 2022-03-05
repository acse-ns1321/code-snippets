import functools
import itertools

# -------------------------------------------------------------------------------------------------------------------------------------
# Initialization
list_a = ['red', 'blue', 'green']                    # manually initialization
list_c = [1, 2, 3, 4, 5]
list_b = list(range(5))                              # initialize from iteratable

# Access element
first_element = list_c[0]                                             # access element
range_of_elements = list_c[1:2]                                           # access a slice of the list
last_element = list_c[-1]                                            # access last element
occurances_of_element = list_a.count("<el>")         # Returns integer number of occurrences. Also works on strings.
element_by_index = list_a.index("<el>")                    # Returns int index of the first occurrence or raises ValueError.

# Add element/ another list
list_a.append("<el>")                                # Or: a += [<el>]
list_b.extend(list_a)                                # Or: a += <collection>

# Concatenation
list_a + list_b                                      # add two lists
h = ['re', 'bl'] + ['gr']                            # list concatenation
i = ['re'] * 5                                       # repeat a list
list_a.insert(1, 'yellow')                           # insert element in specified position

# Delete element
list_a.pop(2)                                        # remove and return item at index (default last)
list_a.remove("<el>")                                # Removes first occurrence of the item or raises ValueError.
list_a.clear()                                       # Removes all items. Also works on dictionary and set.

# -------------------------------------------------------------------------------------------------------------------------------------
# List comprehension
# -------------------------------------------------------------------------------------------------------------------------------------
b = [x for x in range(3)]                           # list comprehension

# -------------------------------------------------------------------------------------------------------------------------------------
# OPERATIONS
# -------------------------------------------------------------------------------------------------------------------------------------

# Sorting
list_a.sort()                                       # Sorts in ascending order.
sorted_list = sorted(list_a)                        # Returns a new sorted list.

# Special Sorts
sorted_by_second = sorted(list_a, key=lambda el: el[1])
sorted_by_both   = sorted(list_a, key=lambda el: (el[1], el[0]))

# Reversing
list_a.reverse()                                  # Reverses the list in-place.
reversed_iter = reversed(list_a)                  # Returns reversed iterator.

# Sum 
sum_of_elements  = sum(list_a)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]

# Product
product_of_elems = functools.reduce(lambda output, el: output * el, list_a) # import functools

# Flatten list
flatter_list  = list(itertools.chain.from_iterable(list_a)) # import itertools

# Check if element is in the list
're' in ['re', 'bl']                             # true if 're' in list
'fi' not in ['re', 'bl']                         # true if 'fi' not in list