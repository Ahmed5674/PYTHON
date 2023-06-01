# Write a program to print the name.

print ("Ahmed")


# Write a program for a Single line comment and multi-line comments.

# Read the input from the user
user_input = input("Enter your comment: ")

# Split the input into lines
lines = user_input.split('\n')

# Check the number of lines
if len(lines) == 1:
    print("Single line comment")
else:
    print("Multi-line comment")


# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = -5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 5
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4      #Value of 'a' modified
    print('Inside h() : ', a)
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

