import os
def print_file_content(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

file_name = "data.txt"
print_file_content(file_name)


