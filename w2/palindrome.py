def is_palindrome(number):
    return str(number) == str(number)[::-1]

print(is_palindrome(526625))

print(is_palindrome(526825))