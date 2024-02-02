def check_for_primes(arr):
    primes_arr = []
    for i in arr:
        if is_prime(i):
            primes_arr.append(i)
    return primes_arr

def is_prime(number):
    if number <= 1:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True

print(check_for_primes([1,2,3,4,5,6,7,8,9,10]))

print(check_for_primes([21,58,57,91,74,67,12,11]))