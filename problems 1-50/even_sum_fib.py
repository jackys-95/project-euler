def fib_even_sum(n):
    return fib_tail(0, 1, n, 0)

def fib_even_sum_tail(a, b, n, even_sum):
    even_sum += a if a % 2 == 0 else 0
    return fib_tail(b, a + b, n - 1, even_sum) if n > 0 else a

def fib_even_sum_iter(n, a, b):
    even_sum = 0
    while b < n:
        a, b = b, a+b
        even_sum += a if a % 2 == 0 else 0
    return even_sum

     
        
        
        
