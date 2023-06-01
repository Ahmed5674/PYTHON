# Open the file in read mode
file = open("filename.txt", "r")

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Print the contents
print(contents)


# Open the file in write mode
  file = open("filename.txt", "w")

  # Write text to the file
  file.write("Hello, this is a text file.")

  # Close the file
  file.close()

# Open the file in read mode
file = open("filename.txt", "r")

# Read the file stream line by line
line = file.readline()
while line:
    print(line)
    line = file.readline()

# Close the file
file.close()

# Open the file in read mode
file = open("filename.txt", "rb")

# Read the file stream using random access
file.seek(10)  # Move to a specific position in the file
contents = file.read(20)  # Read 20 bytes from that position
print(contents)

# Close the file
file.close()

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


import os

# Check file read access
readable = os.access("filename.txt", os.R_OK)
print("Read Access:", readable)

# Check file write access
writable = os.access("filename.txt", os.W_OK)
print("Write Access:", writable)

