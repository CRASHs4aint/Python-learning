s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.replace(" ","").lower()) == sorted(s2.replace(" ","").lower()):
    print("Anagram")
else:
    print("Not anagram")
