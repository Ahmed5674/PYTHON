# Write a function to add integer values of an array.

from audioop import avg
from operator import index
from turtle import position
from typing import final

#Initialize array 
arr = [10,20,30,40]
sum = 0
#Loop through the array to calculate sum of elements 
for i in range(0,len(arr)):
    sum = sum + arr[i]
print("Sum of all integer values in array: ",sum) 

# Write a function to calculate the average value of an array of integers.

def cal_average(num):
    sum_num = 0
    #Loop through the array to average value of elements 
    for i in num:
        sum_num = sum_num + i          

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average([10,21,32,43,54]))

# Write a program to find the index of an array element.

#Initialize array
arr = [1,3,5,3,1,2,6,5,3,8,6,9]

#printing element at specific index in array
index = arr.index(3)
print("Index of 3: ",index)

index = arr.index(9)
print("Index of 9: ",index)

index = arr.index(8)
print("Index of 8: ",index)

# Write a function to test if array contains a specific value.

#Initialize array
arr = [4,5,45,40,50]
#Loop through array to test if array contains a specific value
for num in arr:
    if num == 5:
        print("Element exist")

# Write a function to remove a specific element from an array.

#Initialize array
arr = [44,55,0,15,19,5,4]

#removing a specific element from an array
arr.remove(0)
print(arr)

# Write a function to copy an array to another array

#Initialize array
arr = ['k','a','s','h','i']
arr1 = [] #creating empy array
arr1 = arr.copy() #copying/duplicating arr in arr1
print(arr1)

# Write a function to insert an element at a specific position in the array.

#Initialize array
arr = [101,303,404,505,606,707,808,909]
arr.insert(1,202) #insert 202 at index 1 in arr
print(arr)

# Write a function to find the minimum and maximum value of an array.

#Initialize array
arr = [100,3,3000,20,500,9999,10000,10003]

#minimum value of array
minposition = arr.index(min(arr))
print ("The minimum is at position:", minposition)

#maximum value of array
maxposition = arr.index(max(arr))
print ("The maximum is at position::", maxposition)

# Write a function to reverse an array of integer values.

#Initialize array
arr = [9,8,7,6,5]
arr.reverse() #to reverse an array of integer values
print(arr)

# Write a function to find the duplicate values of an array.
 
#Initialize array    
arr = [21,11,31,13,11]
#Using loop to check duplicate values in array
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:",arr[k])

# Write a program to find the common values between two arrays.

#Initialize array
arr = ['k','a','s','h','i']
arr1 = ['s','h','g']
print("Common values in given arrays:",set(arr).intersection(arr1))

# Write a method to remove duplicate elements from an array.

#Initialize array
arr = [11,22,33,11,44,55]
finalarr = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)

# Write a method to find the second largest number in an array.

#Initialize array
arr = [101,404,202,909,606,505,808,303,707]
arr.sort() #Sorting in ascending order. 
print("Second largest number:",arr[-2]) #displaying the second last element.

# Write a method to find number of even number and odd numbers in an array.

#Initialize array
arr = [1,2,3,4,5,6,7,8,9]
evennumbers = 0
oddnumbers = 0
#using loop to find even and odd numbers in array
for i in arr:
    if i % 2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1 
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)

# Write a function to get the difference of largest and smallest value.

#Initialize array
arr = [10,6,11,13,14]
arr.sort() #Sorting in ascending order
print("Diffrence of largest and smallest value:",arr[4]-arr[0])

# Write a method to verify if the array contains two specified elements(12,23).

#Initialize array
arr = [1,12,19,23,33,54]
#using loop to find if array contains specific elements
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")
