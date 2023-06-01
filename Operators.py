# Write a function for arithmetic operators(+,-,*,/)

# Store input numbers:  
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  
# Add two numbers  
sum = float(num1) + float(num2)  
# Subtract two numbers  
min = float(num1) - float(num2)  
# Multiply two numbers  
mul = float(num1) * float(num2)  
#Divide two numbers  
div = float(num1) / float(num2)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  

# Write a method for increment and decrement operators(++, --)

# A sample use of increasing the variable value by one.
a = 0
a += 1
a = a+1
print('The value of a is ',a)
# Use of increment operator, here start = 1,step = 1(by default) and stop = 5 
print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)
#Use of decrement operator, here start = 5, step = -1 and  stop = -1
print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)

# Write a program to find the two numbers equal or not.

a = input('Enter first number: ')
b = input('Enter second number: ')
if a==b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

# Program for relational operators (<,<==, >, >==)

a = 4
b = 5
print(a < b)  #This operator(<) returns True if the left operand is less than the right operand.
print(a <= b) #This operator(<=)returns True if the left operand is less than or equal to the right operand.
print(a > b)  #This operator(>) returns True if the left operand is greater than the right operand.
print(a >= b) #This operator(>=)returns True if the left operand is greater than or equal to the right operand.   
print(a == b) #This operator(==)returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
print(a != b) #This operator(!=)returns True if both the operands are not equal.

# Print the smaller and larger number.

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
#To print larger number
if a > b: 
     print(a, "is greater ")
else:
    print(b, " is greater ")
#To print samller number
if a < b:
     print(a, "is smaller2 ")
else:
    print(b, " is smaller ")         
