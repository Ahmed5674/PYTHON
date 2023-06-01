# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
student_dict = {
    101: "John",
    102: "Alice",
    103: "Bob",
    104: "Emily",
    105: "David"
}

# 1.1. Adding values to the dictionary
student_dict[106] = "Sophia"

# 1.2. Updating values in the dictionary
student_dict[103] = "Charlie"

# 1.3. Accessing the value in the dictionary
print("Name of student with ID 102:", student_dict[102])

# 1.4. Create a nested loop dictionary
nested_dict = {
    'A': {'a': 1, 'b': 2, 'c': 3},
    'B': {'d': 4, 'e': 5, 'f': 6},
    'C': {'g': 7, 'h': 8, 'i': 9}
}

# 1.5. Access the values of nested loop dictionary
print("Value of 'b' in nested dictionary:", nested_dict['A']['b'])

# 1.6. Print the keys present in a particular dictionary
keys = student_dict.keys()
print("Keys in student dictionary:", keys)

# 1.7. Delete a value from a dictionary
del student_dict[104]
print("After deleting student with ID 104:", student_dict)

