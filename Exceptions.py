import os

# 1. Generate Arithmetic Exception without exception handling
result = 10 / 0  # This will raise an ArithmeticError

try:
    # 2. Handle the Arithmetic exception using try-catch block
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic Exception occurred!")

def method_with_exception():
    # 3. Method that throws an exception
    raise Exception("Exception thrown from method")

# 3. Call a method that throws an exception without try block
method_with_exception()

try:
    # 4. Program with multiple catch blocks
    result = 10 / 0
except ZeroDivisionError:
    print("Zero Division Exception occurred!")
except ArithmeticError:
    print("Arithmetic Exception occurred!")

try:
    # 5. Throw an exception with your own message
    raise Exception("Custom Exception")
except Exception as e:
    print("Custom Exception occurred:", str(e))

# 6. Create your own exception
class CustomException(Exception):
    pass

try:
    raise CustomException("Custom Exception")
except CustomException as e:
    print("Custom Exception occurred:", str(e))

try:
    # 8. Generate Arithmetic Exception
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic Exception occurred!")

try:
    # 9. Generate FileNotFoundError
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")

try:
    # 10. Generate ClassNotFoundException
    os.system("java MyClass")
except FileNotFoundError:
    print("Class not found!")

try:
    # 11. Generate IOException
    file = open("readonly_file.txt", "w")
except PermissionError:
    print("IO Exception occurred!")

try:
    # 12. Generate NoSuchFieldException
    my_dict = {"key": "value"}
    value = my_dict["invalid_key"]
except KeyError:
    print("No such field exception occurred!")

finally:
    # 7. Finally block
    print("Finally block executed")


