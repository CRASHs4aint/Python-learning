ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.islower():
    print("Lowercase letter")
elif ch.isupper():
    print("Uppercase letter")
else:
    print("Special character")
