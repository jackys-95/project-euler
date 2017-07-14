def n_product_palindrome(n):
    max_number = int(str(9) * n)
    range_check = int("1" + (str(0) * (n - 1)))
    
    found_palindrome = False
    palindrome = 0
    a = 0
    b = 0
    
    i = max_number
    current = 0
    while i > range_check:
        j = i
        while j > range_check:
            current = i * j 
            found_palindrome = number_is_palindrome(current)
            if found_palindrome and current > palindrome:
                palindrome = current
                a = i
                b = j
            j-= 1
        i-= 1
        
    return (palindrome, a, b) 
        
def number_is_palindrome(n):
    return str(n) == str(n)[::-1]
