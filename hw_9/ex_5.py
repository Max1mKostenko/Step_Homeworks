"""Match Object"""

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object


"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

# Examples


txt2 = "The rain in Spain"
y = re.search(r"\bS\w+", txt2)
print(y.span())

txt3 = "The rain in Spain"
z = re.search(r"\bS\w+", txt3)
print(z.string)

txt4 = "The rain in Spain"
a = re.search(r"\bS\w+", txt4)
print(a.group())
