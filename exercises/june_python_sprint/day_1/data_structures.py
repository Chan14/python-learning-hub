# Day 2 Challenge — List Magic 🎩✨
# Write a function chanchal_gather_fruits that:
# Takes a list of fruit names (strings).
# Adds your favorite fruit(s) to that list.
# Removes any fruit named "banana" (because maybe you’re allergic or just don’t vibe
# with it).
# Returns a sorted list of fruits (alphabetically).
# BONUS: Print the count of fruits before and after the changes, in a fun way.
# Rules:
# Don’t mutate the original list directly — return a new list.
# Use list comprehension somewhere.
# Feel free to spice it with emojis or your unique flair in print statements.
# When you’re ready, drop your function and sample call with output.
# And remember — no peeking, no copy-paste, I want that Chanchal-brand creativity
# shining through! 💡🔥


def chanchal_gather_fruits(fruits: list) -> list:
    favorite_fruits = ["avocado", "grapefruit", "strawberries"]
    all_fruits = [x for x in sorted(fruits + favorite_fruits) if x.lower() != "banana"]
    return all_fruits


print(chanchal_gather_fruits(["apple", "banana", "orange", "plum", "kiwi"]))

# Create a function chanchal_fruit_inventory that:
# Takes a list of fruits (could have duplicates).
# Returns a dictionary mapping each fruit name to how many times it appears in the list.
# Bonus: Print the fruit that appears the most with a fun message.
from collections import defaultdict


def chanchal_fruit_inventory(fruits: list) -> dict:
    fruits_dict = defaultdict(int)
    for fruit in fruits:
        fruit = fruit.lower()
        fruits_dict[fruit] += 1
    return dict(fruits_dict)


result = chanchal_fruit_inventory(
    [
        "apple",
        "avocado",
        "grapefruit",
        "apple",
        "kiwi",
        "kiwi",
        "orange",
        "plum",
        "strawberries",
    ]
)

most_common = max(result.values())
top_fruits = {k for k, v in result.items() if v == most_common}
