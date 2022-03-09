


# Remove Characters/ Whitespace
<str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
<str>  = <str>.strip('<chars>')              # Strips all passed characters from both ends.

# Split the string
<list> = <str>.split()                       # Splits on one or more whitespace characters.
<list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
<list> = <str>.splitlines(keepends=False)    # On [\n\r\f\v\x1c-\x1e\x85\u2028\u2029] and \r\n.

# Join/Concat strings
<str>  = <str>.join(<coll_of_strings>)       # Joins elements using string as a separator.

# Check string presence
<bool> = <sub_str> in <str>                  # Checks if string contains a substring.
<bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
<bool> = <str>.endswith(<sub_str>)           # Pass tuple of strings for multiple options.
<int>  = <str>.find(<sub_str>)               # Returns start index of the first match or -1.
<int>  = <str>.index(<sub_str>)              # Same, but raises ValueError if missing.

# Replace String
<str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.

# Ceeate a table
<str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.

# Convert String
<str>  = chr(<int>)                          # Converts int to Unicode character.
<int>  = ord(<str>)                          # Converts Unicode character to int.

# Also: 'lstrip()', 'rstrip()' and 'rsplit()'.
# Also: 'lower()', 'upper()', 'capitalize()' and 'title()'.

# Property Methods
# +---------------+----------+----------+----------+----------+----------+
# |               | [ !#$%…] | [a-zA-Z] |  [¼½¾]   |  [²³¹]   |  [0-9]   |
# +---------------+----------+----------+----------+----------+----------+
# | isprintable() |   yes    |   yes    |   yes    |   yes    |   yes    |
# | isalnum()     |          |   yes    |   yes    |   yes    |   yes    |
# | isnumeric()   |          |          |   yes    |   yes    |   yes    |
# | isdigit()     |          |          |          |   yes    |   yes    |
# | isdecimal()   |          |          |          |          |   yes    |
# +---------------+----------+----------+----------+----------+----------+
# Also: 'isspace()' checks for '[ \t\n\r\f\v\x1c-\x1f\x85…]'.

