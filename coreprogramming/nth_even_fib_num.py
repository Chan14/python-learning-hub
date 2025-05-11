# Write a function nth_even_fib(k) that returns the k-th even Fibonacci number.
# Examples:
# nth_even_fib(1) → 0
# nth_even_fib(2) → 2
# nth_even_fib(3) → 8
# nth_even_fib(4) → 34
# Constraints
# Use a loop, not recursion.Return -1 if k < 1


def nth_even_fib_num(k):
    if k < 1:
        return -1
    idx, result = 0, 0
    a, b = 0, 1
    while idx < k:
        if b % 2 == 0:
            idx += 1
            result = b
        a, b = b, a + b
    return result
