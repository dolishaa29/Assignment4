# Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line, end='')  # end='' avoids adding extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with the file name
read_file("sample.txt")
