a = 2             # assignment
a += 1            # (*=, /=)   # change and assign
3 + 2             # addition
3 / 2             # integer (python2) or float (python3) division
3 // 2            # integer division
3 * 2             # multiplication
3 ** 2            # exponent
3 % 2             # remainder
abs(a)            # absolute value
1 == 1            # equal
2 > 1             # larger
2 < 1             # smaller
1 != 2            # not equal
1 != 2 and 2 < 3  # logical AND
1 != 2 or 2 < 3   # logical OR
not 1 == 2        # logical NOT
'a' in b          # test if a is in b
a is b            # test if objects point to the same memory (id)

# Bin, Hex
<int> = ±0b<bin>                         # Or: ±0x<hex>
<int> = int('±<bin>', 2)                 # Or: int('±<hex>', 16)
<int> = int('±0b<bin>', 0)               # Or: int('±0x<hex>', 0)
<str> = bin(<int>)                       # Returns '[-]0b<bin>'.


# Bitwise Operators
<int> = <int> & <int>                    # And (0b1100 & 0b1010 == 0b1000).
<int> = <int> | <int>                    # Or  (0b1100 | 0b1010 == 0b1110).
<int> = <int> ^ <int>                    # Xor (0b1100 ^ 0b1010 == 0b0110).
<int> = <int> << n_bits                  # Left shift (>> for right).
<int> = ~<int>                           # Not (also: -<int> - 1).
