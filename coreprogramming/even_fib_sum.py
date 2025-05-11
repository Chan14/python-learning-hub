# Write a function called even_fib_sum(n) that returns the
# sum of all even Fibonacci numbers less than or equal to n.
# Input n = 13
# Output 10 because the even Fibonacci numbers ≤ 13 are: 0, 2, 8 → sum = 10
# Use a loop (no recursion). Don’t use a list to store the whole sequence.
# Make your function clean and efficient.
# 0 1 1 2 3 5 8 13 21 34


def even_fib_sum(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    even_sum = a
    while b <= n:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum


#  print(even_fib_sum(33))
