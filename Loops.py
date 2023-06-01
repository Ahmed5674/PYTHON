# Write a program to print â€œBright IT Careerâ€ ten times using for loop.

from tkinter import N

#Declaring variable
a = "Bright IT Career"
#using loop to print "Bright IT Career" 10 times
for i in range(10):
    print(a)

# Write a program to print 1 to 20 numbers using the while loop.

i = 1
#using loop to print 1 to 20 numbers
while(i<=20):
    print(i)
    i+= 1 

# Program to equal operator and not equal operators.

a = 5
b = 10
print(a ==b) #Equal operator
print(a != b) #Not Equal operator

# Write a program to print the odd and even numbers.

Numbers = [1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ")  
for i in Numbers:     
    if i % 2 == 0:       
        print(i, end =" ")    
print("\nOdd Numbers:")
for i in Numbers:
    if i % 2 != 0:
        print(i, end =" ")
print()

# Write a program to print largest number among three numbers.

k = 40
a = 50
s = 90
if k >= a and k >= s:
    largest = k
elif a >= k and a >= s:
    largest = a
else:
    largest = s
print("Largest number is: ",largest)  

# Write a program to print even number between 10 and 20 using while.

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

# Write a program to print 1 to 10 using the do-while loop statement.

a = 1
print("Print 1 to 10 using the do-while loop statement:",end=" ")
while True:
    print(a,end=" ")
    a = a + 1
    if(a > 10):
        break 
print()

# Write a program to find Armstrong number or not.

a = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")

# Write a program to find the prime or not.

number = int(input("Enter any number to check prime number or not: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

# Write a program to palindrome or not.

n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

# Program to check whether a number is EVEN or ODD.

a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print("{0} is Even ".format(a))
else:
    print("{0} is Odd ".format(a))  
