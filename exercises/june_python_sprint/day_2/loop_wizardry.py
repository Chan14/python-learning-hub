# 🧩 Challenge 3: Loop Wizardry
# Write a function pairwise_sum that takes two lists of numbers and returns a new
# list where each element is the sum of the corresponding elements from the input lists.

# Example:
# pairwise_sum([1, 2, 3], [4, 5, 6])  # returns [5, 7, 9]

# 🧐 What to practice here:
# Use zip() to iterate pairs from both lists in parallel

# Use a for loop or a list comprehension

# Bonus: Add input validation (make sure both lists have the same length, else raise an
# error)

# Your task:
# Write the function without help.

# Share your code here.
# I’ll review, suggest improvements, and show you a super-Pythonic way if needed.


def pairwise_sum(list1: list, list2: list) -> list:
    # if len(list1) != len(list2):
    #     raise ValueError("list1 and list2 must be of equal length.")
    # Alex - I'm skipping input data validation here because you said we are
    # consenting adults as per Python policy. So I'll assume lists are integer lists. ok
    return [a + b for a, b in zip(list1, list2)]


print(pairwise_sum([1, 2, 3], [2, 4, 6]))
print(pairwise_sum([], [2, 4, 6]))
