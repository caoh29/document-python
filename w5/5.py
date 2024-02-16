def is_armstrong(number):
    # Convert the number to a string to determine its length
    num_str = str(number)
    
    # Calculate the number of digits in the number
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of digits raised to the power of the number of digits is equal to the original number
    return armstrong_sum == number

print(is_armstrong(153))

print(is_armstrong(143))