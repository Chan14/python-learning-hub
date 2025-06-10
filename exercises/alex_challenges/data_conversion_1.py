# Task: Write a Python function that takes a list of strings and returns a dictionary where keys
# are string lengths and values are lists of strings of that length.
# Example:
# group_by_length(["apple", "bat", "car", "dog", "apricot"])
# # Output: {5: ['apple'], 3: ['bat', 'car', 'dog'], 7: ['apricot']}

from collections import defaultdict


def group_by_length(data: list) -> dict:
    grouped = defaultdict(list)
    for each in data:
        grouped[len(each)].append(each)
    return dict(grouped)


input_data = ["apple", "bat", "car", "dog", "apricot"]
print(group_by_length(input_data))
