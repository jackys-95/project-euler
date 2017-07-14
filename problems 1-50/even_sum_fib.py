def fib_even_sum(n):
    '''
    n is the max fibonacci value
    '''
    return fib_even_sum_tail(0, 1, n, 0)

def fib_even_sum_tail(a, b, n, even_sum):
    even_sum += a if a % 2 == 0 else 0
    return fib_even_sum_tail(b, a + b, n, even_sum) if b < n else even_sum

def fib_even_sum_iter(n, a, b):
    even_sum = 0
    while b < n:
        a, b = b, a+b
        even_sum += a if a % 2 == 0 else 0
    return even_sum
