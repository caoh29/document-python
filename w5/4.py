def find_max_min(numbers):
    # Initialize variables to store the maximum and minimum values
    max_num = float('-inf')  # Initialize max_num to negative infinity
    min_num = float('inf')   # Initialize min_num to positive infinity
    
    # Iterate through each number in the list
    for num in numbers:
        # Update max_num if the current number is greater than max_num
        if num > max_num:
            max_num = num
        # Update min_num if the current number is less than min_num
        if num < min_num:
            min_num = num
    
    # Return the maximum and minimum numbers found
    return max_num, min_num


input_list = [1, 5, 7, 10] 
max_num, min_num = find_max_min(input_list) # Calls the function to find the maximum and minimum numbers in the list, and assigns its return value to max_num and min_num
print("Maximum number:", max_num) # Prints max number
print("Minimum number:", min_num) # Prints min number
