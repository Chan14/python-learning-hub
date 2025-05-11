# Implement the Fibonacci series
# The Fibonacci sequence is a series of numbers where every number is
# the sum of the two numbers before it. The first two numbers are 0 and 1:
# 0 1 1 2 3 5 8 13
# Problem statement#
# Your task, therefore, is to write the fib() function which takes in a positive integer, n,
# and returns the n-th Fibonacci number.
# However, instead of using recursion, your function must use loops.
# You also need to keep in mind that when the input is less than one,
# your solution should return -1.
# Example input 7, output 8


def fib(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return a
