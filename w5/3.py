def compress_string(input_string):
    compressed_string = ""
    count = 1
    
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # If the current character is the same as the next character, increment the count
        if i < len(input_string) - 1 and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            # If the next character is different or we have reached the end of the string, append the character and its count to the compressed string
            compressed_string += input_string[i] + str(count)
            # Reset the count for the next character
            count = 1
    
    # Return the compressed string only if it is shorter than the original string
    return compressed_string if len(compressed_string) < len(input_string) else input_string


input_string = input("Enter a string: ") # Asks for a string to user
compressed_string = compress_string(input_string) # Calls the function to compress the string, and assigns its return value to compressed_string
print("Compressed string:", compressed_string) # Prints the compressed string
