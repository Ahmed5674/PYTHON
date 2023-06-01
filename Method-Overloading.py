# Method with the same name but different number of parameters of the same type:

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

result1 = add(2, 3)       # Calls the first add method
result2 = add(2, 3, 4)    # Calls the second add method

print(result1)  # Output: 5
print(result2)  # Output: 9
# Method with the same name but different number of parameters of different data types:

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

result1 = add(2, 3)             # Calls the first add method
result2 = add(2, 3, "Hello")    # Calls the second add method

print(result1)  # Output: 5
print(result2)  # Output: 8Hello

# Method with the same name and the same number of parameters of the same type:

def add(a, b):
    return a + b

def add(a, b):
    return a * b

result = add(2, 3)   # Calls the second add method, as it overwrites the first one

print(result)  # Output: 6
