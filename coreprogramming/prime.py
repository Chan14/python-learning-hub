# prime.py


# Standard prime check
def is_prime(n):
    if n <= 1:
        return False
    divisor = 2
    while divisor <= n // divisor:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


# Optimized division-based prime check
def is_prime_optimized_div(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor <= n // divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


# Optimized multiplication-based prime check
def is_prime_optimized_mul(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True
