#  Write and Append Data to a File (without using a function)

# Take user input and write to 'output.txt'
user = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user)

# Append additional data to the same file
additional= input("Enter some more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional)

# Read and display the final content of the file
with open("output.txt", "r") as file:
    for line in file:
        print(line, end='')
