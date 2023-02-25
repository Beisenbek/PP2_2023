import re
text = input()
pattern1 = "[0-9]+"
pattern2 = "\d+"

x1 = re.search(pattern1, text)
print(x1)

x2 = re.search(pattern2, text)
print(x2)

