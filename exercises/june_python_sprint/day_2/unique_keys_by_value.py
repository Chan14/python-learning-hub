# 🔥 Challenge 5: Unique Keys by Value (Set + Sorted)
# Write a Python function that:
# Takes a dictionary data and a target value.
# Finds all keys in data whose values exactly match value.

# Returns:
# A set of these keys (to ensure uniqueness).
# A sorted list of these keys (sorted alphabetically).

# Your function(s) should:
# Use type hints for inputs and outputs.
# Be efficient and Pythonic.
# Include a brief docstring explaining what it does.

from typing import Any


def unique_keys_by_value(data: dict[str, Any], value=Any) -> tuple[set[str], list[str]]:
    """
    Finds all keys in data whose values exactly match the given value.

    Args:
        data (dict[str, Any]): Dictionary to search.
        value (Any): Value to match against dictionary values.

    Returns:
        tuple: A tuple containing:
            - set[str]: A set of unique keys whose values match.
            - list[str]: A sorted list of those unique keys (alphabetically).
    """
    unique_keys = {k for k, v in data.items() if v == value}
    return unique_keys, sorted(list(unique_keys))


if __name__ == "__main__":
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 1,
        "date": 3,
        "elderberry": 2,
        "fig": 4,
    }

keys_set, keys_sorted = unique_keys_by_value(sample_data, 2)
print("Keys with value 2 (set):", keys_set)
print("Keys with value 2 (sorted list):", keys_sorted)


# Test with a value not present
keys_set_empty, keys_sorted_empty = unique_keys_by_value(sample_data, 99)
print("Keys with value 99 (set):", keys_set_empty)
print("Keys with value 99 (sorted list):", keys_sorted_empty)
