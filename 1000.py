import time

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

def get_prime_numbers_with_timelimit(start, end, timelimit=1):
    start_time = time.time()
    prime_numbers = sieve_of_eratosthenes(end)
    prime_numbers = [num for num in prime_numbers if num >= start]
    end_time = time.time()

    execution_time = end_time - start_time

    if execution_time > timelimit:
        return [], execution_time
    else:
        return prime_numbers, execution_time

# Example usage
start_number = 1
end_number = 1000000
prime_list, execution_time = get_prime_numbers_with_timelimit(start_number, end_number, 1)

print("Prime numbers within the range:")
print(prime_list)
print(f"Execution time: {execution_time} seconds")
