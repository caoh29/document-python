def is_prime(number):
    if number <= 1:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


print(is_prime(15))

print(is_prime(11))