# 🧠 CHALLENGE: Word Frequency by First Letter
# You are given a list of words. You need to:
# Count how many times each word appears (👋 hello, Counter).
# Group the words by their first letter (yo, defaultdict(list)).
# Sort each group alphabetically by the word.
# Output the result in a clean format, like:
# A:
#   apple (3)
#   art (1)
# B:
#   banana (2)
#   box (1)
# ...
# sample Input
# words = [
#     'apple', 'banana', 'apple', 'box', 'art', 'banana', 'carrot',
#     'carrot', 'carrot', 'ant', 'box', 'banana', 'apricot'
# ]

# 🔧 Requirements
# Use collections.Counter to get word frequencies.
# Use collections.defaultdict(list) to group by first letter.
# Sort each group’s words alphabetically.
# Don’t use Pandas. This is raw Python muscle-building.
# 🏁 Bonus (Optional)
# Print the groups in alphabetical order of the first letter.
# Align the output nicely like a report.

from collections import Counter, defaultdict

words = [
    "apple",
    "banana",
    "apple",
    "box",
    "art",
    "banana",
    "carrot",
    "carrot",
    "carrot",
    "ant",
    "box",
    "banana",
    "apricot",
]

# Step 1: Count word frequencies
counts = Counter(words)
# print(counts)

# Step 2: Group by first letter
grouped = defaultdict(list)
for word, freq in counts.items():
    grouped[word[0].upper()].append((word, freq))
# print(by_first_letter)

# Step 3: Sort each group
for key in grouped:
    grouped[key].sort()
# print(by_first_letter)

# Step 4: Print result
for letter in sorted(grouped):
    print(f"{letter}:")
    for word, freq in grouped[letter]:
        print(f"\t {word} ({freq})")
