# Program to display all prime numbers between 20 and 50

start = 20
end = 50

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
