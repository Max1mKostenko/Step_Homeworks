"""The findall() Function"""

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt2 = "The rain in Spain"
y = re.findall("Portugal", txt2)
print(y)
