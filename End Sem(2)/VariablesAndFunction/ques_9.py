# Function that returns multiple values

def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul  # returning multiple values

# Calling the function
x, y, z = calculate(10, 5)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)
