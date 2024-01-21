"""The split() Function"""


import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


txt2 = "The rain in Spain"
y = re.split("\s", txt2, 1)
print(y)
