a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))
if(a>b and a>c):
    print("1st number is greatest among all entered number. ")
elif(b>a and b>c):
    print("2nd number is greatest among all entered number. ")
elif(c>b and c>a):
    print("3rd number is greatest among all entered number. ")
else:
    print("All entered number is equal")
