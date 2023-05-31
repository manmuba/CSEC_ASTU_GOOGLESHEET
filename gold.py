def goldbach_conjecture(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if primes[p] == True:
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                primes[i] = False
        p += 1
    # Find two prime numbers that sum up to n with minimum difference
    min_diff = n
    for p in range(2, n+1):
        if primes[p]:
            if primes[n-p]:
                if abs(p - (n-p)) < min_diff:
                    min_diff = abs(p - (n-p))
                    a, b = p, n-p
    print(a, b)
# goldbach_conjecture(100000)

while True:
    n = int(input())
    if(n == -1):
        break
    goldbach_conjecture(n)