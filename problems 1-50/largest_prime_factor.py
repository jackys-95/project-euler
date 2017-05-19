import math

def largest_prime_factor(n):
    return max(find_prime_factors(n))

def find_prime_factors(n):
    sieve = generate_sieve(math.floor(math.sqrt(n)))
    count = len(sieve)
    print('The amount of primes being checked is: ' + str(count))
    current_n_factor = n
    prime_factors = []
    while i < count and current_n_factor != 1:
        if current_n_factor % sieve[i] == 0:
            current_n_factor / sieve[i]
            prime_factors.append(sieve.pop([i]))
            i = 0
        i += 1

def generate_sieve(n):
    '''
    Generates list of prime numbers from 2 to n using
    Sieve of Erasthothenes algorithm.
    '''
    marked = [False for x in range(0, n)]
    marked[0] = True
    primes = [] # primes generated at the end.
    prime_index = 1

    for i in range(0, n):
        if marked[i] != True:
            prime_index = i
            next_multiple_index = 2 * prime_index + 1 # don't mark current prime
            for j in range(next_multiple_index, n, prime_index + 1):
                marked[j] = True
            primes.append(prime_index + 1)
                          
    return primes
