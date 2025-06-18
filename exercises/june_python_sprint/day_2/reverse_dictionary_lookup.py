# 🧩 Challenge 4: Reverse Dictionary Lookup
# Write a function find_keys_by_value that takes a dictionary and a target value,
# and returns a list of all keys that map to that value.

# data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# find_keys_by_value(data, 1)  # returns ['a', 'c']

# 🧠 What this tests:
# Looping through dict.items()

# Conditionals inside loops or list comprehensions

# Returning a list of matches

# ✨ Bonus Pythonic:
# Try both: regular loop first, then list comprehension.

# Think about: What happens if no keys match?

# When you’re ready, write it your way first.
# Then I’ll give feedback + show a couple elegant options (with love).

from typing import Any


# list comprehension
def find_keys_by_value(data: dict[str, Any], value: Any) -> list[str]:
    return [k for k, v in data.items() if v == value]


# loop version
def find_keys_by_value_2(data: dict, value) -> list:
    keys_by_value = []
    for k, v in data.items():
        if v == value:
            keys_by_value.append(k)
    return keys_by_value


# return sorted keys
def find_keys_by_value_sorted(data: dict[str, Any], value: Any) -> list[str]:
    return sorted([k for k, v in data.items() if v == value])


# Using a generator expression
def find_keys_by_value_3(data: dict[str, Any], value: Any):
    return (k for k, v in data.items() if v == value)


data = {"a": 1, "b": 2, "c": 1, "d": 3}
print(find_keys_by_value(data, 1))
print(find_keys_by_value_2(data, 1))
print(find_keys_by_value_sorted(data, 1))
print(list[find_keys_by_value_3(data, 1)])
