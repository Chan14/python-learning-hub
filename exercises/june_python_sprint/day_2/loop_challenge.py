# 🧠 Loop Challenge #1: Word Frequency Counter
# Problem:
# Write a function count_words(text: str) -> dict that takes a paragraph of text and
# returns a dictionary with word frequencies (case-insensitive). Ignore common
# punctuation like , . ! ? and don't use collections.Counter.

# Example:
# text = "Hello, world! Hello again. World?"
# count_words(text)
# # Output: {'hello': 2, 'world': 2, 'again': 1}
# Rules:

# You must use a loop — no one-liners, no built-ins like Counter.
# Don’t use regular expressions yet.
# Focus on clarity and correctness first.
# ✅ You Can Assume:
# The input is a single string of natural language text (i.e., a sentence or paragraph).
# Words are separated by spaces.
# Punctuation marks may appear, but only these: . , ! ? ( ) [ ]
# No weird edge cases like emojis, hyphenated words, contractions, or embedded numbers.

text = "Hello, ()world((! Hello   again. World?"


def clean_text(text: str) -> str:
    if not text:
        return ""
    cleaned_text = []
    for char in text:
        if char in {".", ",", "!", "?", "(", ")", "[", "]"}:
            continue
        cleaned_text.append(char.lower())
    return "".join(cleaned_text)


def word_frequency_counter(text: str) -> dict:
    input_text = clean_text(text)
    if not input_text:
        return {}
    tokens = input_text.split()
    word_count = {}
    for token in tokens:
        word_count[token] = word_count.get(token, 0) + 1
    return word_count


print(word_frequency_counter(text))
