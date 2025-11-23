import re

s = "Hello World"
print(len(re.findall(r"[aeiou]", s, re.I)))
