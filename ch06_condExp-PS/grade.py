a=int(input("Enter your precentage:"))

if(a>90):
    print("your grade is :Ex")
elif(a>=80 and 90>a):
    print("your grade is :A")
elif(a>=70 and 80>a):
    print("your grade is :B")
elif(a>=60 and 70>a):
    print("your grade is :C")
elif(a>=50 and 60>a):
    print("your grade is :D")
else:
    print("Sorry!you are failed.")