def reverse_string_recursive(input_string):
    # Base case: if the string is empty or has only one character, it is already reversed
    if len(input_string) <= 1:
        return input_string
    else:
        # Recursive step: return the last character of the string concatenated with the reverse of the substring excluding the last character
        return input_string[-1] + reverse_string_recursive(input_string[:-1])


input_string = input("Enter a string: ") # Asks for a string to user
reversed_string = reverse_string_recursive(input_string) # Calls the function to reverse the string, and assigns its return value to reversed_string
print("Reversed string:", reversed_string) # Prints the reversed string
