# 1. Different ways creating a string.

string = 'Hello'
print(string)

string = "Hello"
print(string)

string1 = '''World'''
print(string1)

string2 = """Welcome to
           the world of Python""" # triple quotes string can extend multiple lines
print(string2)
print()

# 2.Concatenating two strings using + operator
str1 = string + string1
print("Concatenated two different strings:",str1)
print()

# 3.Finding the length of the string.
print("length of the string:",len(str1))
print()

# 4.Extract a string using Substring
def extract_substring(string, start_index, end_index):
    substring = string[start_index:end_index]
    return substring

# Example usage
input_string = "Hello, World!"
start_index = 7
end_index = 12
result = extract_substring(input_string, start_index, end_index)
print("Original String:", input_string)
print("Substring:", result)

# 5.Searching in strings using index()
str3 = 'kashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))
print()

# 6.Matching a String Against a Regular Expression With matches().
from ast import Str
import re
Substr = 'Madara'
str6 = 'Madara once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr,str6))
print()

# 7.Comparing strings.
str8 = 'Itachi uchiha'
str1 = 'Madara uchiha'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()

# 8.startsWith(), endsWith()and compareTo()
string = 'Minato Namikaze'
print(string.startswith("Minato"))
print(string.endswith("kaze"))
print()

def compare_to(string1, string2):
    if string1 < string2:
        return -1
    elif string1 > string2:
        return 1
    else:
        return 0

# Example usage
string1 = "Hello"
string2 = "World"
result = compare_to(string1, string2)
print("Comparison result:", result)

# 9.Trimming strings with strip().
str7 = 'Hello World hi'
print(str7.strip("hi"))
print()

# 10.Replacing characters in strings with replace()
string = 'Hi World'
print(string.replace("Hi","Hello"))
print()

# 11.Splitting strings with split()
str9 = 'hi-hello-bye'
print(str9.split("-"))
print()

# 12.Converting integer objects to Strings.
numb = 10
numb1 = str(numb)
print(numb1)
print(type(numb1))

print()
# 13.Converting to uppercase and lowercase.
string = 'hello'
string1 = 'WORLD'
print(string.upper())
print(string1.lower())
