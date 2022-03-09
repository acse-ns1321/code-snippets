Regex
import re


<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences with 'new'.
<list>  = re.findall(<regex>, text)            # Returns all occurrences as strings.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to include the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of the pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
<iter>  = re.finditer(<regex>, text)           # Returns all occurrences as match objects.
Argument 'new' can be a function that accepts a match object and returns a string.
Search() and match() return None if they can't find a match.
Argument 'flags=re.IGNORECASE' can be used with all functions.
Argument 'flags=re.MULTILINE' makes '^' and '$' match the start/end of each line.
Argument 'flags=re.DOTALL' makes dot also accept the '\n'.
Use r'\1' or '\\1' for backreference.
Add '?' after an operator to make it non-greedy.