import re

strings = ["apple","banana","sky","orange","bcdf"]

strings_sorted = sorted(strings, key=lambda x: len(re.findall(r"[aeiou]", x, re.I)))
print(strings_sorted)
