def factorial_of(number):
    if number == 0:
        return 1
    else:
        return number * factorial_of(number - 1)


print(factorial_of(10))

print(factorial_of(6))