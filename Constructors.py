#Program to read a text file:
python
Copy code
# Open the file in read mode
file = open("filename.txt", "r")

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Print the contents
print(contents)
Program to write text to a .txt file using write() method:
python
Copy code
# Open the file in write mode
file = open("filename.txt", "w")

# Write text to the file
file.write("Hello, this is a text file.")

# Close the file
file.close()
Program to read a file stream using readline() method:
python
Copy code
# Open the file in read mode
file = open("filename.txt", "r")

# Read the file stream line by line
line = file.readline()
while line:
    print(line)
    line = file.readline()

# Close the file
file.close()
Program to read a file stream that supports random access:
python
Copy code
# Open the file in read mode
file = open("filename.txt", "rb")

# Read the file stream using random access
file.seek(10)  # Move to a specific position in the file
contents = file.read(20)  # Read 20 bytes from that position
print(contents)

# Close the file
file.close()
Program to read a file and adjust to a particular index using seek():
python
Copy code
# Open the file in read mode
file = open("filename.txt", "r")

# Move to a specific index in the file
file.seek(10)

# Read from that position
contents = file.read()

# Close the file
file.close()

# Print the contents
print(contents)
Program to check whether a file has read and write access permissions:
python
Copy code
import os

# Check file read access
readable = os.access("filename.txt", os.R_OK)
print("Read Access:", readable)

# Check file write access
writable = os.access("filename.txt", os.W_OK)
print("Write Access:", writable)
