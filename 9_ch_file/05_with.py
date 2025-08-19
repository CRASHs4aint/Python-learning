f=  open("file.txt", "r")
data=f.read()
print(data)
f.close()

#same can be wrritten using with satatement like this:

with open ("file.txt") as f:
    print(f.read())
    
    #you dont have to explicitly close the file