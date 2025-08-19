

    
    
   
    
def greatest():#function defintion
    
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=int(input("Enter a number:"))

    if(a>b and a>c):
        print(f"{a} is greatest among all number.")
    elif(b>a and b>c):
        print(f"{b} is greatest among all number.")
    elif(c>a and c>b):
        print(f"{c} is greatest among all number.")
    else:
        print("All number is equal to each other")
        
        
greatest()
        
        