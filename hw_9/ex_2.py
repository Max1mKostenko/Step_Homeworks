"""The search() Function"""

import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())


txt2 = "The rain in Spain"
y = re.search("Portugal", txt2)
print(y)
