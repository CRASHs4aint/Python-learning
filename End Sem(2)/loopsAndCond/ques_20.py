import re

s = input("Enter string: ")
sub = input("Enter pattern: ")

if re.search(sub, s):
    print("Substring found")
else:
    print("Not found")
