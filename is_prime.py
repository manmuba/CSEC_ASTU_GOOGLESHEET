# import time

# def is_prime(n):
#     if n <= 1:
#         return False

#     if n <= 3:
#         return True

#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6

#     return True

# def is_prime_with_timelimit(n, timelimit=1):
#     start_time = time.time()
#     result = is_prime(n)
#     end_time = time.time()

#     execution_time = end_time - start_time

#     if execution_time > timelimit:
#         return False, execution_time
#     else:
#         return result, execution_time

# # Example usage
# number = 9999999968
# prime, execution_time = is_prime_with_timelimit(number, 1)

# if prime:
#     print(f"{number} is prime!")
# else:
#     print(f"{number} is not prime!")

# print(f"Execution time: {execution_time} seconds")


import time

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def is_prime_with_timelimit(n, timelimit=1):
    start_time = time.time()
    result = is_prime(n)
    end_time = time.time()

    execution_time = end_time - start_time

    if execution_time > timelimit:
        return False, execution_time
    else:
        return result, execution_time

def get_prime_numbers(start, end, timelimit=1):
    prime_numbers = []
    for number in range(start, end+1):
        prime, execution_time = is_prime_with_timelimit(number, timelimit)
        if prime:
            prime_numbers.append(number)
        if execution_time > timelimit:
            break

    return prime_numbers

# Example usage
start_number = 1
end_number = 100
prime_list = get_prime_numbers(start_number, end_number, 1)

print("Prime numbers within the range:")
print(prime_list)

