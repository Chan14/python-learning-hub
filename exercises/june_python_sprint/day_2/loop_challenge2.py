# 🔄 Challenge 6: Looping with enumerate()
# Let’s build something like:


def find_indexes_of_target(nums: list[int], target: int) -> list[int]:
    """
    Returns a list of indexes where target appears in nums.
    """
    return [idx for idx, val in enumerate(nums) if val == target]


# 📦 Challenge 7: Looping Through Nested Structures
# Something like:
from typing import Any


def flatten(nested: list[list[Any]]) -> list[Any]:
    """
    Flattens a 2D list into a 1D list.
    """
    return [item for sublist in nested for item in sublist]


# 🛠 Challenge 8 (Bonus / Stretch): Dictionary Merge with Conditions


def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Merge two dictionaries by adding values of matching keys.
    Unique keys are included as is.
    """
    keys = d1.keys() | d2.keys()
    return {key: d1.get(key, 0) + d2.get(key, 0) for key in keys}


def merge_dicts_2(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Merge two dictionaries by adding values of matching keys.
    Unique keys are included as is.
    """
    output_dict = {}
    for k, v in d1.items():
        output_dict[k] = v
    for k, v in d2.items():
        output_dict[k] = output_dict.get(k, 0) + v
    return output_dict


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))
print(merge_dicts_2(d1, d2))
