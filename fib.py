def fib(n):
    fib0 = 0
    fib1 = 1
    index = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        while index != n:
            fib = fib0 + fib1
            fib0 = fib1
            fib1 = fib
            index += 1
        return fib
print('Created by lohpidor')