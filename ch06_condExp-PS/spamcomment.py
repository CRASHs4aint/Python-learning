p1="make a lot of money"
p2="buy now"
p3="click here"
p4="subscribe this"

msg=input("Enter ur comment:")
if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("this a spam")

else:
    print("This is not a spam:")