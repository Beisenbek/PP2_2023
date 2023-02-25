import re

txt = "The rain in Spain Seatle"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
