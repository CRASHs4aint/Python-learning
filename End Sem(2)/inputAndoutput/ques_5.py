a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number:"))
c=int(input("Enter a 3rd number:"))

if(a>b and a>c):
    print(f"{a} is largest among all three numbers.")
if(b>c and b>c):
    print(f"{b} is largest among all three numbers.")
if(c>b and c>a):
    print(f"{c} is largest among all three numbers.")
else:
    print("All entered number is eqaul to each other.")