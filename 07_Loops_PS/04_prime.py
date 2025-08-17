n= int(input("Enter a number:"))

for i in range (2,n):
    if(n%i)==0:
        print("Entered number is not prime.")
        break
else:
        print("Entered number is prime.")    