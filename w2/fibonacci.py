def fibonacci(limit):
    fib = []
    a = 0
    b = 1
    for _ in range(limit):
        fib.append(a)
        a = b
        b = a + b
    return fib

print(fibonacci(5))