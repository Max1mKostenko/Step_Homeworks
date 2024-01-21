"""The sub() Function"""


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


txt2 = "The rain in Spain"
y = re.sub("\s", "9", txt2, 2)
print(y)
