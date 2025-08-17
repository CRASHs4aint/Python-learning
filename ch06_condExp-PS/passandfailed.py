import math
a,b,c=map(int,input("Enter three subject marks of a student:").split())

percent=(a+b+c)/3

if((a==b==c==33) and percent<40):
    print("student is passed.")
else:
    print("student is failed.")


